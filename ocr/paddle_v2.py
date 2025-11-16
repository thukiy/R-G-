import os
from PIL import Image
import torch
from transformers import AutoModelForCausalLM, AutoProcessor

# Device wählen: Apple GPU (MPS) falls verfügbar, sonst CPU
DEVICE = "mps" if torch.backends.mps.is_available() else "cpu"
print("✅ Device:", DEVICE)

CHOSEN_TASK = "ocr"  # 'ocr' | 'table' | 'chart' | 'formula'
PROMPTS = {
    "ocr": "OCR:",
    "table": "Table Recognition:",
    "formula": "Formula Recognition:",
    "chart": "Chart Recognition:",
}

model_path = "PaddlePaddle/PaddleOCR-VL"
image_path = "data/Theorie/bild1.jpg"

# Modell + Processor laden
dtype = torch.bfloat16 if DEVICE != "cpu" else torch.float32
print("📦 Lade Modell ...")
model = AutoModelForCausalLM.from_pretrained(
    model_path, trust_remote_code=True, torch_dtype=dtype
).to(DEVICE).eval()
processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)
processor.tokenizer.lang = "latin"
print("✅ Modell geladen")

# Bild vorbereiten
image = Image.open(image_path).convert("RGB")

# Prompt erstellen
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": PROMPTS[CHOSEN_TASK]},
        ],
    }
]
inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
).to(DEVICE)

inputs = {k: v.to(DEVICE) for k, v in inputs.items()} if isinstance(inputs, dict) else {"input_ids": inputs.to(DEVICE)}

# Inferenz
print("🔍 Inferenz läuft ...")
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=1024)
text = processor.batch_decode(outputs, skip_special_tokens=True)[0]

# Ausgabe
out_file = "data/output_vl/bild1_ocr.txt"
os.makedirs(os.path.dirname(out_file), exist_ok=True)
with open(out_file, "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Ergebnis gespeichert:", out_file)
print("\n--- Auszug ---\n")
print(text[:800])
