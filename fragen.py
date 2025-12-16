#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any

import requests
from dotenv import load_dotenv

from bm25_retriever import (
    get_theory_index,
    get_exercise_index,
    BM25Hit,
)

# ========================
#   CONFIG
# ========================

load_dotenv()

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
DEFAULT_TEXT_MODEL = os.environ.get("TEXT_MODEL", "qwen2.5-math:7b")

K_THEORY = 5   # Anzahl Theorie-Chunks pro Frage
K_EX      = 3  # Anzahl Übungs-Chunks pro Frage


# ========================
#   LLM CALL (mit Fallback)
# ========================

def call_llm(prompt: str, model: str) -> str:
    """
    Versucht zuerst /api/chat (neue Ollama-Versionen).
    Wenn 404 -> Fallback auf /api/generate (ältere Ollama-Versionen).
    """
    # 1) Neuer Weg: /api/chat
    try:
        url = f"{OLLAMA_URL}/api/chat"
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Du bist ein mathematischer Tutor (Analysis, Lineare Algebra, Stochastik). "
                        "Erkläre Schritt für Schritt, sauber und verständlich. "
                        "Du darfst LaTeX für Formeln benutzen."
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
        msg = data.get("message", {}).get("content", "")
        if msg:
            return msg.strip()
    except requests.exceptions.HTTPError as e:
        # Wenn Endpoint nicht existiert → Fallback
        if e.response is None or e.response.status_code != 404:
            raise

    # 2) Fallback: /api/generate
    url = f"{OLLAMA_URL}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }
    resp = requests.post(url, json=payload, timeout=600)
    resp.raise_for_status()
    data = resp.json()
    msg = data.get("response", "")
    return msg.strip()


# ========================
#   RETRIEVAL / PROMPT
# ========================

def format_hits_for_prompt(hits: List[BM25Hit], title: str, max_chars: int = 700) -> str:
    lines: List[str] = [f"### {title}"]
    if not hits:
        lines.append("(Keine Treffer gefunden)")
        return "\n".join(lines)

    for i, h in enumerate(hits, start=1):
        m = h.doc.metadata
        snippet = h.doc.text.replace("\n", " ")
        if len(snippet) > max_chars:
            snippet = snippet[:max_chars] + " …"

        heading = m.get("heading") or m.get("h3") or m.get("h2") or m.get("h1")
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


def build_prompt(course: str,
                 question_text: str,
                 theory_hits: List[BM25Hit],
                 exercise_hits: List[BM25Hit]) -> str:
    ctx_theory = format_hits_for_prompt(theory_hits, "Theorie-Kontext")
    ctx_ex = format_hits_for_prompt(exercise_hits, "Übungs-/Aufgaben-Kontext")

    prompt = f"""
Du bist Tutor im Kurs '{course}'.

Unten findest du Auszüge aus Skript (Theorie) und Übungsblättern (inkl. Lösungen).
Diese wurden per OCR aus handschriftlichen Notizen gewonnen und können Fehler enthalten.

Aufgabe:
1. Beantworte die Frage des Studenten auf Deutsch.
2. Nutze zuerst den gegebenen Kontext (Theorie, Aufgaben).
3. Erkläre Schritt für Schritt.
4. Gib am Ende eine kurze Zusammenfassung.

Frage:
\"\"\"{question_text}\"\"\"

Kontext:
---------------------
{ctx_theory}

---------------------
{ctx_ex}

Bitte beantworte die Frage jetzt.
"""
    return prompt.strip()


# ========================
#   BATCH-LOGIK
# ========================

@dataclass
class QAItem:
    id: Any
    frage: str
    answer: str
    meta: Dict[str, Any]


def answer_question_with_rag(course: str,
                             q_id: Any,
                             q_text: str,
                             thema: str | None,
                             schwierigkeitsgrad: str | None,
                             model: str) -> QAItem:
    # Indizes nur einmal pro Scriptlauf laden wäre noch effizienter – hier keep it simple
    idx_theory = get_theory_index(course)
    theory_hits = idx_theory.search(q_text, k=K_THEORY)

    exercise_hits: List[BM25Hit] = []
    try:
        idx_ex = get_exercise_index(course)
        exercise_hits = idx_ex.search(q_text, k=K_EX)
    except KeyError:
        # Kein Übungs-Index für diesen Kurs
        exercise_hits = []

    prompt = build_prompt(course, q_text, theory_hits, exercise_hits)
    answer = call_llm(prompt, model=model)

    meta = {
        "course": course,
        "model": model,
        "thema": thema,
        "schwierigkeitsgrad": schwierigkeitsgrad,
        "used_theory_chunks": len(theory_hits),
        "used_exercise_chunks": len(exercise_hits),
    }

    return QAItem(id=q_id, frage=q_text, answer=answer, meta=meta)


def run_batch(in_path: Path,
              out_path: Path,
              course: str,
              model: str | None = None) -> None:
    if model is None:
        model = DEFAULT_TEXT_MODEL

    data = json.loads(in_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Erwarte eine JSON-Liste von Objekten (jedes mit Feld 'frage').")

    results: List[Dict[str, Any]] = []

    print(f"Starte Batch für Kurs '{course}' mit Modell '{model}'")
    print(f"Fragen-Datei: {in_path}")

    for obj in data:
        q_text = str(obj.get("frage", "")).strip()
        if not q_text:
            continue

        q_id = obj.get("id")
        thema = obj.get("thema")
        schwierigkeitsgrad = obj.get("schwierigkeitsgrad")

        print(f"→ Frage {q_id}: {q_text[:60]}...")

        item = answer_question_with_rag(
            course=course,
            q_id=q_id,
            q_text=q_text,
            thema=thema,
            schwierigkeitsgrad=schwierigkeitsgrad,
            model=model,
        )

        results.append(
            {
                "id": item.id,
                "frage": item.frage,
                "answer": item.answer,
                "meta": item.meta,
            }
        )

    out_obj = {
        "course": course,
        "model": model,
        "items": results,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out_obj, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Fertig. {len(results)} Antworten gespeichert in: {out_path}")


# ========================
#   CLI
# ========================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Batch: Fragen aus JSON beantworten und Antworten als JSON speichern")
    parser.add_argument("--in", dest="input_path", type=Path, required=True, help="Input-JSON mit Fragen")
    parser.add_argument("--out", dest="output_path", type=Path, required=True, help="Output-JSON mit Antworten")
    parser.add_argument("--course", dest="course", required=True, help="Kursname, z.B. analysis1, analysis2, linearealgebra1, stochastik1")
    parser.add_argument("--model", dest="model", default=None, help="Ollama-Modellname, z.B. qwen2.5-math:7b")

    args = parser.parse_args()

    run_batch(
        in_path=args.input_path,
        out_path=args.output_path,
        course=args.course,
        model=args.model,
    )
