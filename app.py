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

import json
from typing import List

# Wie viele Chunks pro Frage im Batch-Eval?
K_THEORY = 5
K_EXERCISE = 3


def _format_hits_for_prompt(hits: List[BM25Hit], title: str, max_chars: int = 700) -> str:
    lines = [f"### {title}"]
    if not hits:
        lines.append("(Keine Treffer gefunden)")
        return "\n".join(lines)

    for i, h in enumerate(hits, start=1):
        m = h.doc.metadata
        snippet = h.doc.text.replace("\n", " ")
        if len(snippet) > max_chars:
            snippet = snippet[:max_chars] + " …"

        heading = (
            m.get("heading")
            or m.get("h3")
            or m.get("h2")
            or m.get("h1")
        )
        source = m.get("source")
        chunk_id = m.get("chunk_id")

        lines.append(f"\n[Hit {i}] score={h.score:.3f}")
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
    reasoning_mode: bool,
) -> str:
    base = _build_rag_prompt(
        course=course,
        question=question,
        theory_hits=theory_hits,
        exercise_hits=exercise_hits,
    )

    if reasoning_mode:
        base += """

---
Zusätzliche Anweisung:
Denke die Aufgabe zuerst in klaren, kleinen Zwischenschritten durch
(du darfst deine Gedanken explizit aufschreiben) und gib danach die
eigentliche Antwort und Zusammenfassung an."""
    else:
        base += """

---
Zusätzliche Anweisung:
Formuliere die Antwort direkt und halte die Erklärung kompakt."""

    return base



def _build_rag_prompt(
    course: str,
    question: str,
    theory_hits: List[BM25Hit],
    exercise_hits: List[BM25Hit],
) -> str:
    ctx_theory = _format_hits_for_prompt(theory_hits, "Theorie-Kontext")
    ctx_ex = _format_hits_for_prompt(exercise_hits, "Übungs-/Aufgaben-Kontext")

    prompt = f"""
Du bist Mathe-Tutor im Kurs '{course}'.

Unten findest du Auszüge aus dem Theorieskript und aus Übungsblättern.
Diese stammen aus OCR von handschriftlichen Notizen und können leichte Fehler enthalten.

Aufgabe:
1. Beantworte die Studentenfrage auf Deutsch.
2. Nutze zuerst den Kontext (Theorie + Übungen).
3. Erkläre den Lösungsweg Schritt für Schritt, aber nicht unnötig lang.
4. Falls die Frage eine Wahr/Falsch-Aussage ist, schreibe zuerst:
   'Die Aussage ist wahr.' oder 'Die Aussage ist falsch.' mit kurzer Begründung.
5. Am Ende eine sehr kurze Zusammenfassung (1–2 Sätze).

STUDENTENFRAGE:
\"\"\"{question}\"\"\"

-------------------------
{ctx_theory}

-------------------------
{ctx_ex}

Bitte beantworte die Frage jetzt.
"""
    return prompt.strip()


def rag_answer_one(question: str, course: str, model: str) -> dict:
    """
    Eine Frage mit BM25+Theorie/Übung (RAG) beantworten.
    Nutzt deinen bm25_retriever und deine bestehende LLM-Funktion.
    Gibt ein dict mit question/answer/meta zurück.
    """
    course = course.lower()

    # Theorie-BM25
    idx_theory = get_theory_index(course)
    theory_hits = idx_theory.search(question, k=K_THEORY)

    # Übungs-BM25 (falls vorhanden)
    exercise_hits: List[BM25Hit] = []
    try:
        idx_ex = get_exercise_index(course)
        exercise_hits = idx_ex.search(question, k=K_EXERCISE)
    except KeyError:
        # z.B. falls für diesen Kurs noch kein exercise-Index existiert
        exercise_hits = []

    prompt = _build_rag_prompt(
        course=course,
        question=question,
        theory_hits=theory_hits,
        exercise_hits=exercise_hits,
    )

    # 🔴 HIER deine vorhandene LLM-Funktion verwenden:
    # z.B. answer = call_llm_ollama(prompt, model=model)
    answer = call_llm_ollama(prompt, model=model)  # ggf. Funktionsnamen anpassen

    return {
        "question": question,
        "answer": answer,
        "meta": {
            "course": course,
            "model": model,
            "used_theory_chunks": len(theory_hits),
            "used_exercise_chunks": len(exercise_hits),
        },
    }


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

def page_batch_json():
    st.subheader("📦 Batch-JSON (E-Fragen → Antworten-JSON)")

    col_settings, col_main = st.columns([1, 2], gap="large")

    # ---------- linke Spalte: Einstellungen ----------
    with col_settings:
        st.markdown("### ⚙️ Einstellungen")

        course = st.selectbox("Kurs", COURSES, index=0, key="batch_course")
        model = st.text_input(
            "Text-LLM (Ollama)",
            value=DEFAULT_TEXT_MODEL,
            key="batch_model",
        )

        k_theory = st.slider(
            "Theorie-Chunks pro Frage",
            1,
            15,
            5,
            key="batch_k_theory",
        )
        k_ex = st.slider(
            "Übungs-Chunks pro Frage",
            0,
            15,
            3,
            key="batch_k_ex",
        )
        use_exercises = st.checkbox(
            "Übungs-Kontext verwenden",
            value=True,
            key="batch_use_ex",
        )
        reasoning_mode = st.checkbox(
            "Reasoning-Mode",
            value=True,
            key="batch_reasoning",
        )

        max_items = st.number_input(
            "Max. Anzahl Fragen im Batch (0 = alle)",
            min_value=0,
            max_value=10000,
            value=0,
            step=10,
            key="batch_max_items",
        )

    # ---------- rechte Spalte: Upload + Start ----------
    with col_main:
        st.markdown("### 📥 JSON mit Fragen hochladen")

        st.markdown(
            "Erwartet wird eine **Liste** von Objekten mit mindestens einem Feld "
            "`\"frage\"` oder `\"question\"`, z.B.:\n\n"
            "```json\n"
            "[\n"
            "  {\"id\": 1, \"frage\": \"Erkläre die Produktregel.\"},\n"
            "  {\"id\": 2, \"frage\": \"Was ist eine Basis in einem Vektorraum?\"}\n"
            "]\n"
            "```"
        )

        uploaded = st.file_uploader(
            "E-Fragen JSON hochladen",
            type=["json"],
            key="batch_file",
        )

        if not uploaded:
            st.info("Bitte lade zuerst eine JSON-Datei hoch.")
            return

        # JSON einlesen
        try:
            data = json.load(uploaded)
        except Exception as e:
            st.error(f"Fehler beim Lesen des JSON: {e}")
            return

        if not isinstance(data, list):
            st.error("Erwarte eine JSON-Liste von Objekten.")
            return

        st.write(f"Gefundene Einträge: {len(data)}")

        if st.button("🚀 Batch starten"):
            # Fragen einsammeln
            questions = []
            for obj in data:
                q_text = obj.get("frage") or obj.get("question")
                if not q_text:
                    continue
                questions.append(
                    {
                        "id": obj.get("id"),
                        "text": str(q_text).strip(),
                    }
                )

            if not questions:
                st.warning("In der Datei wurde kein Feld 'frage' oder 'question' gefunden.")
                return

            limit = max_items if max_items > 0 else len(questions)
            questions = questions[:limit]

            st.write(f"Starte Batch für {len(questions)} Fragen ...")

            results = []
            progress = st.progress(0.0)
            status = st.empty()

            # BM25-Indizes nur einmal laden
            try:
                idx_theory = get_theory_index(course)
            except Exception as e:
                st.error(f"Fehler beim Laden des Theorie-Index: {e}")
                return

            idx_ex = None
            if use_exercises and k_ex > 0:
                try:
                    idx_ex = get_exercise_index(course)
                except KeyError:
                    st.info("Für diesen Kurs ist kein Übungs-Index konfiguriert.")
                    idx_ex = None
                except Exception as e:
                    st.error(f"Fehler beim Laden des Übungs-Index: {e}")
                    idx_ex = None

            # -------- Loop über alle Fragen --------
            for i, item in enumerate(questions, start=1):
                q_id = item["id"]
                q_text = item["text"]

                status.text(f"Frage {i}/{len(questions)}: {q_text[:80]} ...")
                progress.progress(i / len(questions))

                # Retrieval (wie in page_eval)
                try:
                    theory_hits = idx_theory.search(q_text, k=k_theory)
                except Exception as e:
                    st.error(f"Fehler beim Theorie-Retrieval: {e}")
                    return

                exercise_hits: List[BM25Hit] = []
                if idx_ex is not None and use_exercises and k_ex > 0:
                    try:
                        exercise_hits = idx_ex.search(q_text, k=k_ex)
                    except Exception:
                        exercise_hits = []

                # Prompt (nutzt dein existierendes build_prompt)
                prompt = build_prompt(
                    course=course,
                    question=q_text,
                    theory_hits=theory_hits,
                    exercise_hits=exercise_hits if (use_exercises and k_ex > 0) else [],
                    reasoning_mode=reasoning_mode,
                )

                # LLM-Aufruf (dein call_llm_ollama)
                try:
                    answer = call_llm_ollama(
                        prompt,
                        model=model,
                        reasoning_mode=reasoning_mode,
                    )
                except Exception as e:
                    answer = f"[Fehler beim LLM-Aufruf: {e}]"

                results.append(
                    {
                        "id": q_id,
                        "frage": q_text,
                        "answer": answer,
                        "meta": {
                            "course": course,
                            "model": model,
                            "reasoning_mode": reasoning_mode,
                            "used_theory_chunks": len(theory_hits),
                            "used_exercise_chunks": len(exercise_hits),
                        },
                    }
                )

            status.text("Batch abgeschlossen.")
            progress.progress(1.0)

            # Ergebnis-Objekt
            out_obj = {
                "course": course,
                "model": model,
                "num_items": len(results),
                "items": results,
            }

            out_json_str = json.dumps(out_obj, ensure_ascii=False, indent=2)

            st.success(f"Fertig – {len(results)} Fragen beantwortet.")
            st.subheader("📤 Antworten als JSON herunterladen")
            st.download_button(
                "Antworten herunterladen",
                data=out_json_str,
                file_name=f"eval_answers_{course}.json",
                mime="application/json",
            )

            st.subheader("🔎 Vorschau (erste 3)")
            for item in results[:3]:
                st.markdown(f"**Frage (id={item['id']}):** {item['frage']}")
                st.markdown("**Antwort (gekürzt):**")
                text = item["answer"]
                st.write(text[:800] + (" …" if len(text) > 800 else ""))
                st.markdown("---")




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
    ["Tutor", "Evaluation", "Batch-JSON", "Bild-Aufgabe"],
    index=0,
)

if page == "Tutor":
    page_tutor()
elif page == "Evaluation":
    page_eval()
elif page == "Batch-JSON":
    page_batch_json()
elif page == "Bild-Aufgabe":
    page_image()


if __name__ == "__main__":
    main()
