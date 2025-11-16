# pip install -U "paddleocr[doc-parser]"
from paddleocr import PaddleOCRVL

pipeline = PaddleOCRVL()
out = pipeline.predict("data/Theorie/mathe theorie-21.jpg")

for res in out:
    res.print()
    res.save_to_json(save_path="data/output_vl")
    res.save_to_markdown(save_path="data/output_vl")
