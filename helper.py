#!/usr/bin/env python3
import json
import re
from pathlib import Path
import argparse


def extract_endlösung(answer: str) -> str:
    """
    Extrahiert die erste Zeile als Endlösung
    (z.B. 'Die Aussage ist falsch.'), entfernt Markdown-**.
    """
    if not answer:
        return ""

    # Nur nicht-leere Zeilen
    lines = [l.strip() for l in answer.splitlines() if l.strip()]
    if not lines:
        return ""

    first = lines[0]
    # Markdown-Bold entfernen
    first = re.sub(r"\*\*", "", first)
    return first


def make_cot_liste(answer: str):
    """
    Baut eine CoT-Liste aus Absätzen.
    Jeder Absatz (getrennt durch eine Leerzeile) wird ein Eintrag in 'cot_lösung'.
    """
    if not answer:
        return []

    paragraphs = [p.strip() for p in answer.split("\n\n") if p.strip()]
    return paragraphs


def convert_deepseek_to_mistral_structure(in_path: Path, out_path: Path):
    with in_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if "items" not in data:
        raise ValueError("Eingabedatei hat nicht das erwartete DeepSeek-Format (Key 'items' fehlt).")

    output = []
    for item in data["items"]:
        answer = item.get("answer", "")
        converted = {
            "id": item["id"],
            "cot_lösung": make_cot_liste(answer),
            "endlösung": extract_endlösung(answer),
        }
        output.append(converted)

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Konvertierung fertig. Geschrieben nach: {out_path}")


def main():
    parser = argparse.ArgumentParser(
        description="DeepSeek-r1 JSON in die Struktur von mistral_7b_cot.json konvertieren."
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Pfad zu deepseekr1_cot.json",
    )
    parser.add_argument(
        "output",
        type=Path,
        help="Pfad zur Ausgabedatei (z.B. deepseekr1_cot_mistral_format.json)",
    )
    args = parser.parse_args()

    convert_deepseek_to_mistral_structure(args.input, args.output)


if __name__ == "__main__":
    main()
