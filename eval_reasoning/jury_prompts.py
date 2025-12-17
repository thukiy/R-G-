
import json

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

benchmark = load_json("benchmark.json")
mistral = load_json("mistral.json")
deepseek = load_json("deepseek.json")

# Indexing by ID for fast lookup
mistral_by_id = {x["id"]: x for x in mistral}
deepseek_by_id = {x["id"]: x for x in deepseek}

all_prompts = []

for item in benchmark:
    id = item["id"]
    frage = item["frage"]

    mistral_cot = mistral_by_id[id]["cot"]
    deepseek_cot = deepseek_by_id[id]["cot"]

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
