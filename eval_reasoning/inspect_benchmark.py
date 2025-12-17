import json
from pathlib import Path

path = Path("/Users/thuvarakayograjah/RAG_1/R-G-/eval_reasoning/benchmarks.json")  # oder wie deine Datei heißt

with path.open("r", encoding="utf-8") as f:
    data = json.load(f)

print("Typ von data:", type(data))

if isinstance(data, dict):
    print("Keys der Wurzel:", list(data.keys()))
    items = data.get("items") or data.get("data") or []
else:
    items = data

print("Anzahl Einträge:", len(items))

for i, item in enumerate(items[:10], start=1):
    print(f"Eintrag {i}: keys = {list(item.keys())}")
