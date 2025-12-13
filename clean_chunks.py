#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
import tempfile
import os
from typing import Optional


# ==============================
# 1) DeepSeek-Tags entfernen
# ==============================

TAG_REF_RE = re.compile(r"<\|ref\|>.*?<\|/ref\|>", re.DOTALL)
TAG_DET_RE = re.compile(r"<\|det\|>.*?<\|/det\|>", re.DOTALL)

def clean_deepseek_tags(text: str) -> str:
    if not text:
        return text
    text = TAG_REF_RE.sub(" ", text)
    text = TAG_DET_RE.sub(" ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# ==============================
# 2) Kursnamen normalisieren
# ==============================

def normalize_course(course: Optional[str]) -> Optional[str]:
    if not course:
        return course
    c = course.strip()

    mapping = {
        "Stochastic1": "stochastik1",
        "Stochastik1": "stochastik1",
        "Stochastic3": "stochastik3",
        "Stochastik3": "stochastik3",
        "Analysis1": "analysis1",
        "Analysis2": "analysis2",
        "Analysis3": "analysis3",
        "LineareAlgebra1": "linearealgebra1",
        "LineareAlgebra 1": "linearealgebra1",
        "LineareAlgebra2": "linearealgebra2",
        "LineareAlgebra 2": "linearealgebra2",
    }
    return mapping.get(c, c.lower())


def fix_type(meta: dict, forced_type: Optional[str]) -> dict:
    m = dict(meta)
    if forced_type is not None:
        m["type"] = forced_type
    return m


# ==============================
# 3) Ein File säubern (JSONL)
# ==============================

def clean_jsonl_file(
    input_path: Path,
    output_path: Path,
    forced_course: Optional[str] = None,
    forced_type: Optional[str] = None,
) -> None:
    input_path = Path(input_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not input_path.is_file():
        raise FileNotFoundError(f"Input-Datei nicht gefunden: {input_path}")

    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", delete=False,
        dir=str(output_path.parent), suffix=".tmp"
    ) as tf:
        tmp_name = tf.name

        with input_path.open("r", encoding="utf-8") as f_in:
            for line in f_in:
                line = line.strip()
                if not line:
                    continue

                obj = json.loads(line)

                # Inhalt bereinigen
                if "text" in obj:
                    obj["text"] = clean_deepseek_tags(obj["text"])
                elif "content" in obj:
                    obj["content"] = clean_deepseek_tags(obj["content"])

                meta = obj.get("metadata", {})

                # course
                if forced_course is not None:
                    meta["course"] = forced_course
                else:
                    meta["course"] = normalize_course(meta.get("course"))

                # type
                meta = fix_type(meta, forced_type)

                obj["metadata"] = meta

                tf.write(json.dumps(obj, ensure_ascii=False) + "\n")

    os.replace(tmp_name, output_path)
    print(f"→ Bereinigt: {input_path.name}  ->  {output_path}")


# ==============================
# 4) ALLE KURSE KONFIGURIEREN
# ==============================

BASE = Path("/Users/thuvarakayograjah/Documents/RAG/R-G-/data_processed")



CLEAN_JOBS = [
    # ---------- ANALYSIS 1 ----------
    {
        "input":  BASE / "merged_theory" / "Theorie_analysis1_chunks.jsonl",
        "output": BASE / "merged_theory" / "Theorie_analysis1_chunks_clean.jsonl",
        "forced_course": "analysis1",
        "forced_type": "theory",
    },
    {
        "input":  BASE / "merged_exercises" / "Exercise_Analysis1_chunks.jsonl",
        "output": BASE / "merged_exercises" / "Exercise_analysis1_chunks_clean.jsonl",
        "forced_course": "analysis1",
        "forced_type": "exercise",
    },

    # ---------- ANALYSIS 2 ----------
    {
        "input":  BASE / "merged_theory" / "Theorie_Analysis2_chunks.jsonl",
        "output": BASE / "merged_theory" / "Theorie_Analysis2_chunks_clean.jsonl",
        "forced_course": "analysis2",
        "forced_type": "theory",
    },
    {
        "input":  BASE / "merged_exercises" / "Exercise_Analysis2_chunks.jsonl",
        "output": BASE / "merged_exercises" / "Exercise_analysis2_chunks_clean.jsonl",
        "forced_course": "analysis2",
        "forced_type": "exercise",
    },

    # ---------- ANALYSIS 3 ----------
    {
        "input":  BASE / "merged_theory" / "Theorie_Analysis3_chunks.jsonl",
        "output": BASE / "merged_theory" / "Theorie_analysis3_chunks_clean.jsonl",
        "forced_course": "analysis3",
        "forced_type": "theory",
    },
    {
        "input":  BASE / "merged_exercises" / "Exercise_Analysis3_chunks.jsonl",
        "output": BASE / "merged_exercises" / "Exercise_analysis3_chunks_clean.jsonl",
        "forced_course": "analysis3",
        "forced_type": "exercise",
    },

    # ---------- LINEARE ALGEBRA 1 ----------
    {
        "input":  BASE / "merged_theory" / "Theorie_Linear algebra 1_chunks.jsonl",
        "output": BASE / "merged_theory" / "Theorie_linearealgebra1_chunks_clean.jsonl",
        "forced_course": "linearealgebra1",
        "forced_type": "theory",
    },
    {
        "input":  BASE / "merged_exercises" / "Exercise_Linear Algebra1_chunks.jsonl",
        "output": BASE / "merged_exercises" / "Exercise_linearealgebra1_chunks_clean.jsonl",
        "forced_course": "linearealgebra2",
        "forced_type": "exercise",
    },

    # ---------- LINEARE ALGEBRA 2 ----------
    {
        "input":  BASE / "merged_theory" / "Theorie_Linear algebra 2_chunks.jsonl",
        "output": BASE / "merged_theory" / "Theorie_linearealgebra2_chunks_clean.jsonl",
        "forced_course": "linearealgebra2",
        "forced_type": "theory",
    },
    {
        "input":  BASE / "merged_exercises" / "Exercise_Linear algebra2_chunks.jsonl",
        "output": BASE / "merged_exercises" / "Exercise_linearalgebra2_chunks_clean.jsonl",
        "forced_course": "linearealgebra2",
        "forced_type": "exercise",
    },

    # ---------- STOCHASTIK 1 ----------
    {
        "input":  BASE / "merged_theory" / "Theorie_Stochastic 1_chunks.jsonl",
        "output": BASE / "merged_theory" / "Theorie_stochastic1_chunks_clean.jsonl",
        "forced_course": "stochastik1",
        "forced_type": "theory",
    },
    {
        "input":  BASE / "merged_exercises" / "Exercise_Stochastic1_chunks.jsonl",
        "output": BASE / "merged_exercises" / "Exercise_Stochastic1_chunks_clean.jsonl",
        "forced_course": "stochastik1",
        "forced_type": "exercise",
    },

    # ---------- STOCHASTIK 3 ----------
    {
        "input":  BASE / "merged_theory" / "Theorie_Stochastic 3_chunks.jsonl",
        "output": BASE / "merged_theory" / "Theorie_Stochastic3_chunks_clean.jsonl",
        "forced_course": "stochastik3",
        "forced_type": "theory",
    },
    {
        "input":  BASE / "merged_exercises" / "Exercise_Stochastic 3_chunks.jsonl",
        "output": BASE / "merged_exercises" / "Exercise_Stochastic3_chunks_clean.jsonl",
        "forced_course": "stochastik3",
        "forced_type": "exercise",
    },
]


def main():
    for job in CLEAN_JOBS:
        try:
            clean_jsonl_file(
                input_path=job["input"],
                output_path=job["output"],
                forced_course=job.get("forced_course"),
                forced_type=job.get("forced_type"),
            )
        except FileNotFoundError as e:
            print(f"⚠️  Überspringe (Datei fehlt): {e}")
        except Exception as e:
            print(f"⚠️  Fehler bei {job['input']}: {e}")


if __name__ == "__main__":
    main()
