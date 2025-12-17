#!/usr/bin/env python3
"""
judge_runner.py

- Lädt Benchmark + Modell-Outputs
- Baut für jede Aufgabe 2 Prompts (A/B & B/A)
- Ruft den Judge über judge_api.call_judge_model()
- Speichert alle Roh-Antworten in judge_raw_results.json
"""

from pathlib import Path
from typing import List, Dict, Any
import json


from judge_api import call_judge_model_novita  # aus judge_api.py

# -----------------------
# KONFIGURATION
# -----------------------

# Ordner, in dem dieses Skript liegt
BASE_DIR = Path(__file__).resolve().parent

# Dateinamen ggf. anpassen
FILE_BENCHMARK = BASE_DIR / "benchmarks.json"
FILE_MODEL_A = BASE_DIR / "mistral.json"
FILE_MODEL_B = BASE_DIR / "deepseek.json"

MODEL_A_NAME = "Mistral 7B"
MODEL_B_NAME = "DeepSeek R1"

OUTPUT_RAW_RESULTS = BASE_DIR / "judge_raw_results.json"

def build_messages(
    frage: str,
    modell_a: str,
    cot_a: str,
    end_a: str,
    modell_b: str,
    cot_b: str,
    end_b: str,
) -> List[Dict[str, str]]:
    user_prompt = USER_TEMPLATE.format(
        frage=frage,
        modell_a=modell_a,
        cot_a=cot_a,
        end_a=end_a,
        modell_b=modell_b,
        cot_b=cot_b,
        end_b=end_b,
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
# -----------------------
# PROMPT-VORLAGEN
# -----------------------

SYSTEM_PROMPT = """Du bist ein hochqualifizierter, unvoreingenommener Experte für mathematisches Reasoning und Logik.

Deine Aufgabe ist es, zwei Lösungen (Antwort A und Antwort B) für dieselbe mathematische Aufgabe zu vergleichen.

Bewertungskriterien:

1. Du bewertest ausschließlich die Qualität der logischen Argumentation (Chain-of-Thought, CoT).
2. Eine korrekte Endlösung allein reicht nicht aus; der gesamte Lösungsweg muss schlüssig, präzise und fehlerfrei sein.
3. Falls beide Lösungen zur korrekten Endlösung führen:
   – Wähle die Lösung mit dem klareren, effizienteren und besser begründeten Lösungsweg.
4. Falls beide Lösungen fehlerhaft sind:
   – Wähle die Lösung, deren Fehler am geringsten ist oder deren Ansatz dem korrekten Lösungsweg am nächsten kommt.
5. Du kennst die Ground Truth nicht und darfst sie nicht verwenden; bewerte nur die gezeigten Lösungswege.

WICHTIG:
- Sei strikt, präzise und konsistent.
- Deine finale Ausgabe MUSS ein valides JSON-Objekt sein, exakt im vorgegebenen Format.
"""

USER_TEMPLATE = """Frage:
{frage}

---
ANTWORT A (Modell: {modell_a})
Lösungsweg:
{cot_a}

Endlösung:
{end_a}

---
ANTWORT B (Modell: {modell_b})
Lösungsweg:
{cot_b}

Endlösung:
{end_b}

---

AUFGABE FÜR DICH:

1. Analysiere zuerst Antwort A:
   - Identifiziere Stärken und Schwächen des Reasonings.
   - Prüfe jeden Schritt auf logische Konsistenz und rechnerische Korrektheit.

2. Analysiere danach Antwort B:
   - Identifiziere Stärken und Schwächen des Reasonings.
   - Prüfe jeden Schritt auf logische Konsistenz und rechnerische Korrektheit.

3. Vergleiche beide Antworten:
   - Entscheide auf Grundlage der Argumentationsqualität, welches Modell das bessere mathematische Reasoning gezeigt hat.
   - Wähle "UNENTSCHIEDEN" nur, wenn beide Lösungen in Qualität und Korrektheit praktisch gleichwertig sind.

4. WICHTIG:
   - Du kennst die Ground Truth NICHT und darfst sie nicht verwenden.
   - Triff deine Entscheidung nur anhand der gezeigten Lösungswege und Endlösungen.

GIB NUR EIN EINZIGES JSON-OBJEKT ZURÜCK, KEINEN ERKLÄRENDEN TEXT AUSSERHALB DES JSON.

Das JSON-Format lautet GENAU so:

```json
{{
  "analyse_antwort_a": "Kurze, präzise Zusammenfassung der Stärken/Schwächen von Antwort A.",
  "analyse_antwort_b": "Kurze, präzise Zusammenfassung der Stärken/Schwächen von Antwort B.",
  "ausfuehrliche_begruendung_urteil": "Vergleichende Begründung, warum A oder B (oder UNENTSCHIEDEN) gewählt wurde.",
  "gewaehlte_antwort": "A",
  "gewaehltes_modell": "{modell_a}"
}}"""


# Dateien prüfen
for path in [FILE_BENCHMARK, FILE_MODEL_A, FILE_MODEL_B]:
    if not path.exists():
        raise FileNotFoundError(f"Datei nicht gefunden: {path}")

print("[judge_runner] Lade JSON-Dateien ...")
benchmark = load_json(FILE_BENCHMARK)
  # nur 3 Aufgaben, also 6 API-Calls

model_a_data = load_json(FILE_MODEL_A)
model_b_data = load_json(FILE_MODEL_B)

# Index nach id
a_by_id = {item["id"]: item for item in model_a_data}
b_by_id = {item["id"]: item for item in model_b_data}

results = []
total = len(benchmark)
print(f"[judge_runner] Starte Adjudication für {total} Aufgaben ...")

for idx, task in enumerate(benchmark, start=1):
    task_id = task["id"]
    frage = task["frage"]

    a = a_by_id[task_id]
    b = b_by_id[task_id]

    cot_a = a["cot_lösung"]
    cot_b = b["cot_lösung"]
    end_a = a["endlösung"]
    end_b = b["endlösung"]

    # --- Prompt 1: A = Modell A, B = Modell B ---
    msgs_ab = build_messages(
        frage=frage,
        modell_a=MODEL_A_NAME,
        cot_a=cot_a,
        end_a=end_a,
        modell_b=MODEL_B_NAME,
        cot_b=cot_b,
        end_b=end_b,
    )
    print(f"[judge_runner] (id={task_id}) Sende Prompt AB an Judge...")
    raw_ab = call_judge_model_novita(msgs_ab)
    results.append(
        {
            "id": task_id,
            "order": f"{MODEL_A_NAME}__{MODEL_B_NAME}",
            "modell_a": MODEL_A_NAME,
            "modell_b": MODEL_B_NAME,
            "judge_output": raw_ab,
        }
    )

    # --- Prompt 2: A = Modell B, B = Modell A ---
    msgs_ba = build_messages(
        frage=frage,
        modell_a=MODEL_B_NAME,
        cot_a=cot_b,
        end_a=end_b,
        modell_b=MODEL_A_NAME,
        cot_b=cot_a,
        end_b=end_a,
    )
    print(f"[judge_runner] (id={task_id}) Sende Prompt BA an Judge...")
    raw_ba = call_judge_model_novita(msgs_ba)
    results.append(
        {
            "id": task_id,
            "order": f"{MODEL_B_NAME}__{MODEL_A_NAME}",
            "modell_a": MODEL_B_NAME,
            "modell_b": MODEL_A_NAME,
            "judge_output": raw_ba,
        }
    )

    if idx % 10 == 0 or idx == total:
        print(f"[judge_runner] Fortschritt: {idx}/{total} Aufgaben abgeschlossen")

print(f"[judge_runner] Speichere Roh-Ergebnisse nach {OUTPUT_RAW_RESULTS} ...")
with OUTPUT_RAW_RESULTS.open("w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("[judge_runner] Fertig ✅")
