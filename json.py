#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def iter_question_objects(obj: Any):
    """
    Durchläuft eine beliebig verschachtelte Struktur (dict/list)
    und liefert alle dicts, die ein Feld 'frage' enthalten.
    """
    if isinstance(obj, dict):
        if "frage" in obj:
            yield obj
        for v in obj.values():
            yield from iter_question_objects(v)
    elif isinstance(obj, list):
        for el in obj:
            yield from iter_question_objects(el)


def extract_questions(in_path: Path, out_path: Path) -> None:
    # Datei laden
    raw = in_path.read_text(encoding="utf-8")
    data = json.loads(raw)

    result: List[Dict[str, Any]] = []

    for obj in iter_question_objects(data):
        frage = str(obj.get("frage", "")).strip()
        if not frage:
            continue

        # Nur die wichtigsten Felder übernehmen
        result.append(
            {
                "id": obj.get("id"),
                "thema": obj.get("thema"),
                "schwierigkeitsgrad": obj.get("schwierigkeitsgrad"),
                "frage": frage,
            }
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"✅ {len(result)} Fragen gespeichert in: {out_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fragen aus JSON extrahieren")
    parser.add_argument(
        "--in",
        dest="input_path",
        type=Path,
        required=True,
        help="Pfad zur ursprünglichen JSON-Datei",
    )
    parser.add_argument(
        "--out",
        dest="output_path",
        type=Path,
        required=True,
        help="Pfad für die neue Fragen-JSON",
    )

    args = parser.parse_args()
    extract_questions(args.input_path, args.output_path)
