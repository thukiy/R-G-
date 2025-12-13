
from __future__ import annotations

import textwrap
from typing import List

import requests
import streamlit as st

from bm25_retriever import (
    get_theory_index,
    get_exercise_index,
    BM25Hit,
)



OLLAMA_URL = "http://localhost:11434"


DEFAULT_MODEL = "qwen2.5"

COURSES = [
    "analysis1",
    "analysis2",
    "analysis3",
    "linearealgebra1",
    "linearealgebra2",
    "stochastik1",
    "stochastik3",
]



def call_llm_ollama(prompt: str, model: str) -> str:
    """
    Ruft ein Chat-/LLM-Modell via Ollama /api/chat auf und gibt die gesamte Antwort zurück.
    Kein Streaming (für einfachere Integration in Streamlit).
    """
    url = f"{OLLAMA_URL}/api/chat"

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Du bist ein mathematischer Tutor an einer Hochschule. "
                    "Du erklärst Analysis, Lineare Algebra und Stochastik verständlich und Schritt für Schritt. "
                    "Nutze den gegebenen Kontext, aber erfinde keine Fakten, die nicht durch den Kontext gestützt werden. "
                    "Wenn etwas im Kontext nicht steht, kannst du dein eigenes Wissen nutzen, "
                    "aber kennzeichne das dann klar."
                ),
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
    # Für /api/chat: Antwort steht in data["message"]["content"]
    msg = data.get("message", {}).get("content", "")
    return msg.strip()




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
) -> str:
    course = course.lower()
    ctx_theory = format_hits_for_prompt(theory_hits, "Theorie-Kontext")
    ctx_ex = format_hits_for_prompt(exercise_hits, "Übungs-/Aufgaben-Kontext")

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
    6. Versuche am Ende eine kurze Zusammenfassung zu geben.

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



def main():
    st.set_page_config(page_title="Math RAG Tutor (BM25 + Ollama)", layout="wide")

    st.title("🧠 Math RAG Tutor")
    st.write("BM25-Retrieval auf deinen Chunks + Ollama-LLM als Tutor.")


    with st.sidebar:
        st.header("⚙️ Einstellungen")

        course = st.selectbox(
            "Kurs",
            COURSES,
            index=COURSES.index("analysis1") if "analysis1" in COURSES else 0,
        )

        model = st.text_input("Ollama Modell", value=DEFAULT_MODEL, help="z.B. 'qwen2.5', 'llama3.1', 'deepseek-r1'")

        k_theory = st.slider("Anzahl Theorie-Chunks", 1, 15, 5)
        k_ex = st.slider("Anzahl Übungs-Chunks", 0, 15, 5)
        use_exercises = st.checkbox("Übungs-Chunks als Kontext verwenden", value=True)

        st.markdown("---")
        st.markdown("**Ollama-Server:**")
        st.code(OLLAMA_URL, language="bash")


    st.subheader("❓ Deine Frage / Aufgabe")

    default_question = "Erkläre die Produktregel und gib ein Beispiel."
    question = st.text_area(
        "Formuliere hier deine Frage oder kopiere eine Aufgabenstellung hinein:",
        value=default_question,
        height=120,
    )

    if st.button("🔍 Frage beantworten"):
        if not question.strip():
            st.warning("Bitte gib eine Frage ein.")
            return

        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown("### 🔎 Retrieval (BM25)")
            st.write(f"Kurs: `{course}`")

            # Theorie-Retrieval
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

            # Übungs-Retrieval
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

        with col2:
            st.markdown("### 🤖 Tutor-Antwort")

            with st.spinner("LLM denkt nach..."):
                try:
                    prompt = build_prompt(
                        course=course,
                        question=question,
                        theory_hits=theory_hits,
                        exercise_hits=exercise_hits if use_exercises else [],
                    )
                    answer = call_llm_ollama(prompt, model=model)
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


if __name__ == "__main__":
    main()
