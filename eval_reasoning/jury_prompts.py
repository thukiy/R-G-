
import json

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Template for generating judge prompts
JUDGE_PROMPT_TEMPLATE = """
Du bist ein hochqualifizierter, unvoreingenommener Experte für mathematisches Reasoning und Logik.

Deine Aufgabe ist es, zwei Lösungen (Antwort A und Antwort B) für dieselbe mathematische Aufgabe zu vergleichen.

Bewertungskriterien:

1. Du bewertest ausschließlich die Qualität der logischen Argumentation (Chain-of-Thought, CoT).
2. Eine korrekte Endlösung allein reicht nicht aus; der gesamte Lösungsweg muss schlüssig, präzise und fehlerfrei sein.
3. Falls beide Lösungen zur korrekten Endlösung führen:
   – Wähle die Lösung mit dem klareren, effizienteren und besser begründeten Lösungsweg.
4. Falls beide Lösungen fehlerhaft sind:
   – Wähle die Lösung, deren Fehler am geringsten ist oder deren Ansatz dem korrekten Lösungsweg am nächsten kommt.
5. Du darfst die korrekte Lösung NICHT „raten“ oder bekannte Benchmarks „wiedererkennen“; bewerte nur auf Basis der präsentierten Lösungswege.

WICHTIG:
- Sei strikt, präzise und konsistent.
- Deine finale Ausgabe MUSS ein valides JSON-Objekt sein, exakt im vorgegebenen Format.

"""

benchmark = load_json("/Users/thuvarakayograjah/RAG_1/R-G-/eval_reasoning/benchmarks.json")
mistral = load_json("/Users/thuvarakayograjah/RAG_1/R-G-/eval_reasoning/mistral.json")
deepseek = load_json("/Users/thuvarakayograjah/RAG_1/R-G-/eval_reasoning/deepseek.json")

# Indexing by ID for fast lookup
mistral_by_id = {x["id"]: x for x in mistral}
deepseek_by_id = {x["id"]: x for x in deepseek}

all_prompts = []

for item in benchmark:
    id = item["id"]
    frage = item["frage"]

    mistral_cot = mistral_by_id[id]["cot_lösung"]
    deepseek_cot = deepseek_by_id[id]["cot_lösung"]

    # Prompt 1: A=Mistral, B=DeepSeek
    prompt_AB = JUDGE_PROMPT_TEMPLATE.format(
        frage=frage,
        modell_A="Mistral",
        cot_A=mistral_cot,
        modell_B="DeepSeek",
        cot_B=deepseek_cot
    )

    # Prompt 2: A=DeepSeek, B=Mistral
    prompt_BA = JUDGE_PROMPT_TEMPLATE.format(
        frage=frage,
        modell_A="DeepSeek",
        cot_A=deepseek_cot,
        modell_B="Mistral",
        cot_B=mistral_cot
    )

    all_prompts.append({
        "id": id,
        "order": "Mistral-DeepSeek",
        "prompt": prompt_AB
    })
    all_prompts.append({
        "id": id,
        "order": "DeepSeek-Mistral",
        "prompt": prompt_BA
    })

# Save prompts
with open("judge_prompts.json", "w", encoding="utf-8") as f:
    json.dump(all_prompts, f, ensure_ascii=False, indent=2)
