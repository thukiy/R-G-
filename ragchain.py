
from __future__ import annotations

import argparse
import textwrap
from typing import List

import requests

from bm25_retriever import (
    get_theory_index,
    get_exercise_index,
    BM25Hit,
)




OLLAMA_URL = "http://localhost:11434"


LLM_MODEL = "qwen2.5"




def call_llm_ollama(prompt: str, model: str = LLM_MODEL) -> str:
    """
    Ruft ein Chat-/LLM-Modell via Ollama /api/chat auf und gibt die gesamte Antwort zurück.
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
        "stream": True,
    }

    response = requests.post(url, json=payload, stream=True)
    response.raise_for_status()

    full_answer = ""
    for line in response.iter_lines():
        if not line:
            continue
        try:
            obj = line.decode("utf-8")
            data = None
            # Ollama schickt pro Zeile ein JSON
            import json as _json
            data = _json.loads(obj)
        except Exception:
            continue

        delta = data.get("message", {}).get("content", "")
        full_answer += delta

    return full_answer.strip()




def format_hits(hits: List[BM25Hit], title: str, max_chars_per_hit: int = 700) -> str:
    """
    Formatiert BM25-Treffer als Textblock für den Prompt.
    """
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
    """
    Baut einen Prompt für das LLM:
      - Kontext: Theorie + Übungen
      - Frage des Nutzers
      - klare Instruktion: Schritt-für-Schritt-Erklärung
    """
    course = course.lower()
    ctx_theory = format_hits(theory_hits, "Theorie-Kontext")
    ctx_ex = format_hits(exercise_hits, "Übungs-/Aufgaben-Kontext")

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


# ========================
#   MAIN LOGIK
# ========================

def main():
    parser = argparse.ArgumentParser(
        description="Mathe-Tutor mit BM25-Retrieval (Theorie + Übung) und Ollama-LLM."
    )
    parser.add_argument(
        "--course",
        type=str,
        required=True,
        help="Kursname, z.B. 'analysis1', 'analysis2', 'analysis3', 'linearealgebra1', 'linearealgebra2', 'stochastik1', 'stochastik3'.",
    )
    parser.add_argument(
        "--question",
        "-q",
        type=str,
        required=True,
        help="Frage / Aufgabe, die du stellen willst.",
    )
    parser.add_argument(
        "--k-theory",
        type=int,
        default=5,
        help="Anzahl der Theorie-Treffer (BM25).",
    )
    parser.add_argument(
        "--k-exercise",
        type=int,
        default=5,
        help="Anzahl der Übungs-Treffer (BM25).",
    )
    parser.add_argument(
        "--no-exercises",
        action="store_true",
        help="Nur Theorie als Kontext verwenden (keine Übungs-Chunks).",
    )

    args = parser.parse_args()
    course = args.course.lower()
    question = args.question

    print(f"Course: {course}")
    print(f"Frage: {question}")
    print("Suche relevante Theorie-Chunks (BM25)...")

    # 1) Theorie-Retriever
    idx_theory = get_theory_index(course)
    theory_hits = idx_theory.search(question, k=args.k_theory)

    # 2) Übungs-Retriever (optional)
    exercise_hits: List[BM25Hit] = []
    if not args.no_exercises:
        try:
            idx_ex = get_exercise_index(course)
            exercise_hits = idx_ex.search(question, k=args.k_exercise)
        except KeyError:
            print("Hinweis: Für diesen Kurs ist kein Übungs-Index konfiguriert.")
            exercise_hits = []

    # 3) Prompt bauen
    prompt = build_prompt(course, question, theory_hits, exercise_hits)

    # Optional: Debug-Ausgabe
    print("\n================ PROMPT AN LLM ================\n")
    print(prompt)
    print("\n================ ANTWORT VOM LLM ==============\n")

    # 4) LLM aufrufen
    answer = call_llm_ollama(prompt)
    print(answer)


if __name__ == "__main__":
    main()
