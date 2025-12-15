from __future__ import annotations

import base64
import io
import os
import textwrap
from typing import List

import requests
import streamlit as st
from PIL import Image
from dotenv import load_dotenv

load_dotenv()  # .env einlesen

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
DEFAULT_TEXT_MODEL = os.environ.get("TEXT_MODEL", "deepseek-r1:32b")
DEFAULT_VISION_MODEL = os.environ.get("VISION_MODEL", "qwen2.5-vl")


from bm25_retriever import (
    get_theory_index,
    get_exercise_index,
    BM25Hit,
)

# ========================
#   BASIS-KONFIG
# ========================



COURSES = [
    "analysis1",
    "analysis2",
    "analysis3",
    "linearealgebra1",
    "linearealgebra2",
    "stochastik1",
    "stochastik3",
]


# ========================
#   LLM CALLS (OLLAMA)
# ========================

def call_llm_ollama(prompt: str, model: str, reasoning_mode: bool = False) -> str:
    """
    Ruft ein Chat-/LLM-Modell via Ollama /api/chat auf und gibt die Antwort zurück.
    reasoning_mode: verstärkt Schritt-für-Schritt-Erklärungen im Systemprompt.
    """
    system_content = (
    "Du bist ein mathematischer Tutor an einer Hochschule. "
    "Du erklärst Analysis, Lineare Algebra und Stochastik verständlich und Schritt für Schritt. "
    "Nutze den gegebenen Kontext, aber erfinde keine Fakten, die nicht durch den Kontext gestützt werden. "
    "Wenn etwas im Kontext nicht steht, kannst du dein eigenes Wissen nutzen, "
    "aber kennzeichne das dann klar. "
    "Du darfst LaTeX für Formeln benutzen, z.B. f(x) = x^2 als $f(x) = x^2$ oder "
    "$$\\int_0^1 x^2\\,dx$$ für Integrale."
)


    
    if reasoning_mode:
        system_content += (
            " Gib deine Erklärung besonders detailliert und geordnet an. "
            "Gehe in nummerierten Schritten vor (Schritt 1, Schritt 2, …) und erkläre, "
            "warum du jeden Schritt machst."
        )

    url = f"{OLLAMA_URL}/api/chat"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_content,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "stream": False,
    }

    resp = requests.post(url, json=payload, timeout=600)
    resp.raise_for_status()
    data = resp.json()
    msg = data.get("message", {}).get("content", "")
    return msg.strip()


def call_vision_llm_ollama(image_b64: str, question: str, model: str) -> str:
    """
    Ruft ein Vision-LLM via Ollama /api/chat auf.
    Das Bild wird als base64-String übergeben.
    """
    url = f"{OLLAMA_URL}/api/chat"

    system_content = (
        "Du bist ein mathematischer Tutor. "
        "Du bekommst ein Bild mit einer mathematischen Aufgabe (z.B. handschriftlich). "
        "1. Lies die Aufgabe sorgfältig vom Bild ab. "
        "2. Formuliere die Aufgabe kurz in Textform nach. "
        "3. Löse die Aufgabe Schritt für Schritt. "
        "4. Erkläre die wichtigsten Zwischenschritte in Worten. "
        "4. Wenn du Rechenwege erklärst, schreibe die wichtigsten Formeln explizit hin."
        "Du darfst LaTeX benutzen, z.B. $f(x) = x^2 + 3x$ oder $$\\int_0^1 x^2\\,dx$$ für Integrale."
        "Falls Teile des Bildes unleserlich sind, sage das offen."
        "6. Gib am Ende eine kurze Zusammenfassung der Lösung."
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_content},
            {
                "role": "user",
                "content": question,
                "images": [image_b64],
            },
        ],
        "stream": False,
    }

    resp = requests.post(url, json=payload, timeout=600)
    resp.raise_for_status()
    data = resp.json()
    msg = data.get("message", {}).get("content", "")
    return msg.strip()


# ========================
#   RETRIEVAL / KONTEXT
# ========================

def format_hits_for_prompt(hits: List[BM25Hit], title: str, max_chars_per_hit: int = 700) -> str:
    lines: List[str] = []
    lines.append(f"### {title}")
    if not hits:
        lines.append("(Keine Treffer gefunden)")
        return "\n".join(lines)

    for i, h in enumerate(hits, start=1):
        m = h.doc.metadata
        snippet = h.doc.text.replace("\n", " ")
        if len(snippet) > max_chars_per_hit:
            snippet = snippet[:max_chars_per_hit] + " …"

        heading = m.get("heading") or m.get("h3") or m.get("h2") or m.get("h1")
        source = m.get("source")
        course = m.get("course")
        chunk_id = m.get("chunk_id")

        lines.append(f"\n[Hit {i}] score={h.score:.3f}")
        if course:
            lines.append(f"  course: {course}")
        if source:
            lines.append(f"  source: {source}")
        if chunk_id is not None:
            lines.append(f"  chunk_id: {chunk_id}")
        if heading:
            lines.append(f"  heading: {heading}")
        lines.append("  text: " + snippet)

    return "\n".join(lines)


def build_prompt(
    course: str,
    question: str,
    theory_hits: List[BM25Hit],
    exercise_hits: List[BM25Hit],
    reasoning_mode: bool = False,
) -> str:
    course = course.lower()
    ctx_theory = format_hits_for_prompt(theory_hits, "Theorie-Kontext")
    ctx_ex = format_hits_for_prompt(exercise_hits, "Übungs-/Aufgaben-Kontext")

    extra_instr = ""
    if reasoning_mode:
        extra_instr = (
            "\n    WICHTIG: Erkläre deinen Lösungsweg in klar nummerierten Schritten (Schritt 1, Schritt 2, ...). "
            "Benutze kurze Zwischenüberschriften, wo sinnvoll."
        )

    instruction = textwrap.dedent(f"""
    Du bist ein Tutor für den Kurs '{course}'. Unten findest du Auszüge aus Skript (Theorie)
    und aus Übungsblättern (inkl. Lösungen). Diese Auszüge stammen aus handschriftlichem
    Material, das per OCR verarbeitet wurde, und können daher Fehler enthalten.

    Deine Aufgabe:
    1. Beantworte die folgende Studentenfrage auf Deutsch.
    2. Nutze zuerst den gegebenen Kontext (Theorie und Übungen).
    3. Erkläre den Lösungsweg Schritt für Schritt, als würdest du einem Kommilitonen helfen.
    4. Wenn du Rechenwege erklärst, schreibe die wichtigsten Formeln explizit hin (LaTeX-Style \\( ... \\) ist ok).
    5. Wenn der Kontext etwas nicht hergibt, darfst du dein eigenes Wissen nutzen, kennzeichne das aber z.B. mit
       'Zusätzliches Wissen:'.
    6. Versuche am Ende eine kurze Zusammenfassung zu geben.{extra_instr}

    Studentenfrage:
    \"\"\"{question}\"\"\"

    Verfügbarer Kontext:
    ---------------------
    {ctx_theory}

    ---------------------
    {ctx_ex}

    Bitte antworte jetzt.
    """)

    return instruction.strip()


# ========================
#   STREAMLIT PAGES
# ========================

def page_tutor():
    st.subheader("🎓 Tutor-Modus (Textfrage)")

    col_settings, col_main = st.columns([1, 2], gap="large")

    with col_settings:
        st.markdown("### ⚙️ Einstellungen")

        course = st.selectbox("Kurs", COURSES, index=0)
        model = st.text_input("Text-LLM (Ollama)", value=DEFAULT_TEXT_MODEL)
        k_theory = st.slider("Anzahl Theorie-Chunks", 1, 15, 5)
        k_ex = st.slider("Anzahl Übungs-Chunks", 0, 15, 5)
        use_exercises = st.checkbox("Übungs-Chunks als Kontext verwenden", value=True)
        reasoning_mode = st.checkbox("Reasoning-Mode (extra Schritt-für-Schritt)", value=True)

    with col_main:
        st.markdown("### ❓ Deine Frage / Aufgabe")
        default_question = "Erkläre die Produktregel und gib ein Beispiel."
        question = st.text_area(
            "Formuliere hier deine Frage oder kopiere eine Aufgabenstellung hinein:",
            value=default_question,
            height=140,
        )

        if st.button("🔍 Beantworten", type="primary"):
            if not question.strip():
                st.warning("Bitte gib eine Frage ein.")
                return

            col_retr, col_answer = st.columns([1, 1])

            with col_retr:
                st.markdown("### 🔎 Retrieval (BM25)")
                st.write(f"Kurs: `{course}`")

                # Theorie
                st.write("**Theorie-Chunks holen...**")
                try:
                    idx_theory = get_theory_index(course)
                except Exception as e:
                    st.error(f"Fehler beim Laden des Theorie-Index: {e}")
                    return

                theory_hits = idx_theory.search(question, k=k_theory)

                with st.expander("📘 Gefundene Theorie-Chunks", expanded=True):
                    if not theory_hits:
                        st.write("_Keine Theorie-Treffer gefunden._")
                    else:
                        for i, h in enumerate(theory_hits, start=1):
                            m = h.doc.metadata
                            heading = m.get("heading") or m.get("h3") or m.get("h2") or m.get("h1")
                            title = f"[{i}] score={h.score:.3f} – {heading or 'Ohne Überschrift'}"
                            with st.expander(title, expanded=False):
                                st.write(f"**Quelle:** {m.get('source')}")
                                st.write(f"**Chunk ID:** {m.get('chunk_id')}")
                                st.write("---")
                                st.text(h.doc.text)

                # Übungen
                exercise_hits: List[BM25Hit] = []
                if use_exercises and k_ex > 0:
                    st.write("**Übungs-Chunks holen...**")
                    try:
                        idx_ex = get_exercise_index(course)
                        exercise_hits = idx_ex.search(question, k=k_ex)
                    except KeyError:
                        st.info("Für diesen Kurs ist kein Übungs-Index konfiguriert.")
                        exercise_hits = []
                    except Exception as e:
                        st.error(f"Fehler beim Laden des Übungs-Index: {e}")
                        exercise_hits = []

                    with st.expander("📗 Gefundene Übungs-/Lösungs-Chunks", expanded=False):
                        if not exercise_hits:
                            st.write("_Keine Übungs-Treffer gefunden._")
                        else:
                            for i, h in enumerate(exercise_hits, start=1):
                                m = h.doc.metadata
                                heading = m.get("heading") or m.get("h3") or m.get("h2") or m.get("h1")
                                title = f"[{i}] score={h.score:.3f} – {heading or 'Ohne Überschrift'}"
                                with st.expander(title, expanded=False):
                                    st.write(f"**Quelle:** {m.get('source')}")
                                    st.write(f"**Chunk ID:** {m.get('chunk_id')}")
                                    st.write("---")
                                    st.text(h.doc.text)

            with col_answer:
                st.markdown("### 🤖 Tutor-Antwort")
                with st.spinner("LLM denkt nach..."):
                    try:
                        prompt = build_prompt(
                            course=course,
                            question=question,
                            theory_hits=theory_hits,
                            exercise_hits=exercise_hits if (use_exercises and k_ex > 0) else [],
                            reasoning_mode=reasoning_mode,
                        )
                        answer = call_llm_ollama(prompt, model=model, reasoning_mode=reasoning_mode)
                    except requests.exceptions.RequestException as e:
                        st.error(f"Ollama-Request fehlgeschlagen: {e}")
                        return
                    except Exception as e:
                        st.error(f"Fehler beim LLM-Aufruf: {e}")
                        return

                st.markdown("#### Antwort")
                st.markdown(answer)

                with st.expander("📜 Verwendeter Prompt (Debug)", expanded=False):
                    st.text(prompt)


def page_eval():
    st.subheader("📊 Eval-Modus (mehrere Fragen testen)")

    col_settings, col_main = st.columns([1, 2], gap="large")

    with col_settings:
        st.markdown("### ⚙️ Einstellungen")
        course = st.selectbox("Kurs", COURSES, index=0, key="eval_course")
        model = st.text_input("Text-LLM (Ollama)", value=DEFAULT_TEXT_MODEL, key="eval_model")
        k_theory = st.slider("Theorie-Chunks pro Frage", 1, 15, 5, key="eval_k_theory")
        k_ex = st.slider("Übungs-Chunks pro Frage", 0, 15, 3, key="eval_k_ex")
        use_exercises = st.checkbox("Übungs-Kontext verwenden", value=True, key="eval_use_ex")
        reasoning_mode = st.checkbox("Reasoning-Mode", value=True, key="eval_reasoning")

    with col_main:
        st.markdown("### ❓ Fragenliste")

        st.markdown(
            "Gib mehrere Fragen ein, **je eine pro Zeile**. "
            "Die App beantwortet jede Frage nacheinander und zeigt eine Liste der Antworten an."
        )

        default_questions = "Erkläre die Produktregel.\nWas ist eine Basis in einem Vektorraum?\nWas ist die hypergeometrische Verteilung?"
        questions_raw = st.text_area(
            "Fragen (eine pro Zeile):",
            value=default_questions,
            height=180,
        )

        if st.button("🚀 Eval starten"):
            questions = [q.strip() for q in questions_raw.splitlines() if q.strip()]
            if not questions:
                st.warning("Bitte gib mindestens eine Frage ein.")
                return

            results = []
            progress = st.progress(0.0)
            status = st.empty()

            for i, q in enumerate(questions, start=1):
                status.text(f"Frage {i}/{len(questions)}: {q[:80]}...")
                progress.progress(i / len(questions))

                # Retrieval
                try:
                    idx_theory = get_theory_index(course)
                    theory_hits = idx_theory.search(q, k=k_theory)
                except Exception as e:
                    st.error(f"Fehler beim Theorie-Index: {e}")
                    return

                exercise_hits: List[BM25Hit] = []
                if use_exercises and k_ex > 0:
                    try:
                        idx_ex = get_exercise_index(course)
                        exercise_hits = idx_ex.search(q, k=k_ex)
                    except Exception:
                        exercise_hits = []

                prompt = build_prompt(
                    course=course,
                    question=q,
                    theory_hits=theory_hits,
                    exercise_hits=exercise_hits if (use_exercises and k_ex > 0) else [],
                    reasoning_mode=reasoning_mode,
                )

                try:
                    answer = call_llm_ollama(prompt, model=model, reasoning_mode=reasoning_mode)
                except Exception as e:
                    answer = f"[Fehler beim LLM-Aufruf: {e}]"

                results.append((q, answer))

            status.text("Eval abgeschlossen.")
            progress.progress(1.0)

            st.markdown("### Ergebnisse")
            for i, (q, ans) in enumerate(results, start=1):
                with st.expander(f"Frage {i}: {q}", expanded=False):
                    st.markdown("**Antwort:**")
                    st.markdown(ans)


def page_image():
    st.subheader("🖼️ Bild-Modus (Aufgabe als Bild)")

    col_settings, col_main = st.columns([1, 2], gap="large")

    with col_settings:
        st.markdown("### ⚙️ Einstellungen")
        vision_model = st.text_input("Vision-LLM (Ollama)", value=DEFAULT_VISION_MODEL)
        default_question = (
            "Lies die Aufgabe von dem Bild ab, formuliere sie kurz in Textform "
            "und löse sie Schritt für Schritt."
        )
        user_question = st.text_area(
            "Instruktion an das Modell:",
            value=default_question,
            height=120,
        )

    with col_main:
        st.markdown("### 📤 Bild-Upload")

        uploaded = st.file_uploader(
            "Lade ein Bild mit einer mathematischen Aufgabe hoch (JPG/PNG):",
            type=["jpg", "jpeg", "png"],
        )

        if uploaded is not None:
            # Vorschau
            image = Image.open(uploaded)
            st.image(image, caption="Hochgeladenes Bild", use_column_width=True)

            if st.button("🧠 Aufgabe vom Bild lösen", type="primary"):
                # In base64 konvertieren
                buf = io.BytesIO()
                image.save(buf, format="PNG")
                img_bytes = buf.getvalue()
                img_b64 = base64.b64encode(img_bytes).decode("utf-8")

                with st.spinner("Vision-LLM analysiert das Bild..."):
                    try:
                        answer = call_vision_llm_ollama(
                            image_b64=img_b64,
                            question=user_question,
                            model=vision_model,
                        )
                    except requests.exceptions.RequestException as e:
                        st.error(f"Ollama-Request fehlgeschlagen: {e}")
                        return
                    except Exception as e:
                        st.error(f"Fehler beim Vision-LLM-Aufruf: {e}")
                        return

                st.markdown("### 🧾 Antwort des Tutors")
                st.markdown(answer)
        else:
            st.info("Bitte lade zuerst ein Bild hoch.")


# ========================
#   MAIN
# ========================

def main():
    st.set_page_config(page_title="Math RAG Tutor (BM25 + Ollama)", layout="wide")

    st.title("🧠 Math RAG Tutor")
    st.write("BM25-Retrieval auf deinen Chunks + Ollama (Text & Vision) als Tutor.")

    # Seitenwahl
    page = st.sidebar.radio(
        "Modus",
        ["Tutor", "Evaluation", "Bild-Aufgabe"],
        index=0,
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Ollama-Endpoint:**")
    st.sidebar.code(OLLAMA_URL)

    if page == "Tutor":
        page_tutor()
    elif page == "Evaluation":
        page_eval()
    elif page == "Bild-Aufgabe":
        page_image()


if __name__ == "__main__":
    main()
