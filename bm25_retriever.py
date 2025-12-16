#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any, Literal

from rank_bm25 import BM25Okapi


# =========================
#   KONFIGURATION
# =========================

# Basis-Ordner, unter dem deine Chunks liegen
BASE_DATA_DIR_THE = Path("/Users/isabellenachbaur/Documents/GitHub/R-G-/data_processed/")
BASE_DATA_DIR_EXE = Path("/Users/isabellenachbaur/Documents/GitHub/R-G-/data_processed/")

"""
BM25_SOURCES:
- Key: kursname (alles lowercase, z.B. "analysis1", "linearealgebra1", "stochastik1")
- pro Kurs:
    - "theory": Pfad zur Theorie-Chunks-Datei (.json oder .jsonl)
    - "exercise": Pfad zur Übungs-Chunks-Datei (.json oder .jsonl)

!!! HIER PFADNAMEN ANPASSEN, SO, WIE DU SIE WIRKLICH HAST !!!
"""

BM25_SOURCES: Dict[str, Dict[str, Path]] = {
    # ==== ANALYSIS 1 ====
    "analysis1": {
        # Beispiel: aus build_theory_chunks für Analysis1
        "theory": BASE_DATA_DIR_THE / "merged_theory" / "Theorie_analysis1_chunks_clean.jsonl",
        # Beispiel: deine gespeicherten Übungs-Chunks
        "exercise": BASE_DATA_DIR_EXE/ "merged_exercises" / "Exercise_analysis1_chunks_clean.jsonl",
    },

    # ==== ANALYSIS 2 ====
    "analysis2": {
        "theory": BASE_DATA_DIR_THE / "merged_theory" / "Theorie_Analysis2_chunks_clean.jsonl",
        "exercise": BASE_DATA_DIR_EXE / "merged_exercises" / "Exercise_analysis2_chunks_clean.jsonl",
    },

    # ==== ANALYSIS 3 ====
    "analysis3": {
        "theory": BASE_DATA_DIR_THE / "merged_theory" / "Theorie_analysis3_chunks_clean.jsonl",
        "exercise": BASE_DATA_DIR_EXE / "merged_exercises" / "Exercise_analysis3_chunks_clean.jsonl",
    },

    # ==== LINEARE ALGEBRA 1 ====
    "linearealgebra1": {
        "theory": BASE_DATA_DIR_THE / "merged_theory" / "Theorie_linearalgebra1_chunks_clean.jsonl",
        "exercise": BASE_DATA_DIR_EXE / "merged_exercises" / "Exercise_linearealgebra1_chunks_clean.json",
    },

    # ==== LINEARE ALGEBRA 2 ====
    "linearealgebra2": {
        "theory": BASE_DATA_DIR_THE / "merged_theory" / "Theorie_linearealgebra2_chunks_clean.jsonl",
        "exercise": BASE_DATA_DIR_EXE / "merged_exercises" / "Exercise_linearalgebra2_chunks_clean.jsonl",
    },

    # ==== STOCHASTIK 1 ====
    "stochastik1": {
        "theory": BASE_DATA_DIR_THE / "merged_theory" / "Theorie_stochastic1_chunks_clean.jsonl",
        "exercise": BASE_DATA_DIR_EXE / "merged_exercises" / "Exercise_Stochastic1_chunks_clean.jsonl",
    },

    # ==== STOCHASTIK 3 ====
    "stochastik3": {
        "theory": BASE_DATA_DIR_THE / "merged_theory" / "Theorie_Stochastic3_chunks_clean.jsonl",
        "exercise": BASE_DATA_DIR_EXE / "merged_exercises" / "Exercise_Stochastic3_chunks_clean.json",
    },
}


# =========================
#   DATENKLASSEN
# =========================

@dataclass
class BM25Doc:
    doc_id: str
    text: str
    metadata: Dict[str, Any]


@dataclass
class BM25Hit:
    doc: BM25Doc
    score: float


class BM25Index:
    """
    Einfacher BM25-Index über deine Chunks.
    """

    def __init__(self, docs: List[BM25Doc]):
        self.docs: List[BM25Doc] = docs
        self._tokenized_docs: List[List[str]] = [self._tokenize(d.text) for d in docs]
        self._bm25 = BM25Okapi(self._tokenized_docs)

    # --- Tokenizer (simpel – aber reicht) ---
    @staticmethod
    def _tokenize(text: str) -> List[str]:
        text = text.lower()
        # alles, was kein Buchstabe/Zahl/äöüß ist, durch Leerzeichen ersetzen
        text = re.sub(r"[^a-z0-9äöüß]+", " ", text)
        tokens = text.split()
        return tokens

    # --- Suche ---
    def search(self, query: str, k: int = 5) -> List[BM25Hit]:
        tokens = self._tokenize(query)
        scores = self._bm25.get_scores(tokens)
        idx_sorted = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]

        hits: List[BM25Hit] = []
        for i in idx_sorted:
            hits.append(BM25Hit(doc=self.docs[i], score=float(scores[i])))
        return hits


# =========================
#   JSON / JSONL LADEN
# =========================

def load_docs_from_jsonl(path: Path) -> List[BM25Doc]:
    """
    Erwartet JSONL-Zeilen wie:
      {"id": "...", "text": "...", "metadata": {...}}
    oder
      {"content": "...", "metadata": {...}}
    """
    docs: List[BM25Doc] = []

    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                print(f"⚠️  JSON-Fehler in {path} Zeile {i}, überspringe.")
                continue

            text = obj.get("text") or obj.get("content") or ""
            meta = obj.get("metadata") or {}
            doc_id = str(obj.get("id") or meta.get("id") or f"line-{i}")

            docs.append(BM25Doc(doc_id=doc_id, text=text, metadata=meta))

    return docs


def load_docs_from_json(path: Path) -> List[BM25Doc]:
    """
    Erwartet JSON-Array mit Objekten wie:
      [{"content": "...", "metadata": {...}}, ...]
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Erwarte Liste von Records in JSON: {path}")

    docs: List[BM25Doc] = []
    for i, obj in enumerate(data, start=1):
        text = obj.get("text") or obj.get("content") or ""
        meta = obj.get("metadata") or {}
        doc_id = str(obj.get("id") or meta.get("id") or f"item-{i}")

        docs.append(BM25Doc(doc_id=doc_id, text=text, metadata=meta))

    return docs


def load_docs_for(course: str, kind: Literal["theory", "exercise"]) -> List[BM25Doc]:
    """
    Lädt Dokumente für einen Kurs & Typ:
      - course: "analysis1", "analysis2", "analysis3",
                "linearealgebra1", "linearealgebra2",
                "stochastik1", "stochastik3"
      - kind:   "theory" oder "exercise"
    """
    course_key = course.lower()
    cfg = BM25_SOURCES.get(course_key)
    if not cfg:
        raise KeyError(f"Kein Eintrag für course={course_key!r} in BM25_SOURCES")

    path = cfg.get(kind)
    if not path:
        raise KeyError(f"Kein Pfad für {course_key}.{kind} in BM25_SOURCES")

    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Datei nicht gefunden: {path}")

    if path.suffix.lower() == ".jsonl":
        return load_docs_from_jsonl(path)
    elif path.suffix.lower() == ".json":
        return load_docs_from_json(path)
    else:
        raise ValueError(f"Unbekanntes Format (erwarte .json oder .jsonl): {path}")


# =========================
#   INDEX-CACHE & API
# =========================

_BM25_CACHE: Dict[str, BM25Index] = {}  # course_kind → BM25Index


def get_index(course: str, kind: Literal["theory", "exercise"]) -> BM25Index:
    key = f"{course.lower()}_{kind}"
    if key in _BM25_CACHE:
        return _BM25_CACHE[key]

    docs = load_docs_for(course, kind)
    idx = BM25Index(docs)
    _BM25_CACHE[key] = idx
    return idx


def get_theory_index(course: str) -> BM25Index:
    return get_index(course, "theory")


def get_exercise_index(course: str) -> BM25Index:
    return get_index(course, "exercise")


# =========================
#   SELF-TEST
# =========================

def _print_hits(title: str, hits: List[BM25Hit], max_chars: int = 200):
    print(f"\n=== {title} (n={len(hits)}) ===")
    for i, h in enumerate(hits, start=1):
        m = h.doc.metadata
        snippet = h.doc.text.replace("\n", " ")
        if len(snippet) > max_chars:
            snippet = snippet[:max_chars] + " …"

        print(f"[{i}] id={h.doc.doc_id}  score={h.score:.3f}")
        print("   source:", m.get("source"))
        print("   type:", m.get("type"))
        print("   heading:", m.get("heading") or m.get("h2") or m.get("h1"))
        print("   text:", snippet)
        print()


if __name__ == "__main__":
    query = "Erkläre die Produktregel und gib ein Beispiel."

    # Beispiel: Analysis 3 Theorie
    try:
        idx_theory = get_theory_index("analysis3")
        hits_theory = idx_theory.search(query, k=5)
        _print_hits("Analysis3 Theorie", hits_theory)
    except Exception as e:
        print("⚠️  Fehler bei Theorie-Index:", e)

    # Beispiel: Analysis 3 Übungen
    try:
        idx_ex = get_exercise_index("analysis3")
        hits_ex = idx_ex.search(query, k=5)
        _print_hits("Analysis3 Übungen", hits_ex)
    except Exception as e:
        print("⚠️  Fehler bei Übungs-Index:", e)
