#!/usr/bin/env python3
from __future__ import annotations

import argparse
import io
import json
import os
import socket
import time
from pathlib import Path
from typing import List, Dict, Any

import replicate
from pdf2image import convert_from_path
from pydantic import BaseModel
from PIL import Image


class PDFPageOutput(BaseModel):
    page_number: int
    markdown: str
    raw_page_json: dict


class PDFDocumentOutput(BaseModel):
    file_name: str
    pages: List[PDFPageOutput]


class DeepSeekOCRProcessorReplicate:
    """
    OCR-Wrapper für DeepSeek-OCR auf Replicate.
    - Kann einzelne Bilder (JPG/PNG) verarbeiten
    - Kann PDFs per pdf2image -> PIL -> DeepSeek verarbeiten
    - Schreibt alle Outputs flach in output_dir (keine Unterordner)
    """

    def __init__(
        self,
        model_ref: str,
        output_dir: Path,
        dpi: int = 220,
        task_key: str = "task_type",
        task_value: str = "Convert to Markdown",
        max_retries: int = 3,
        retry_delay: float = 5.0,
    ):
        token = os.getenv("REPLICATE_API_TOKEN")
        if not token:
            raise RuntimeError("Bitte REPLICATE_API_TOKEN als Environment-Variable setzen.")
        # Client initialisieren
        self.client = replicate.Client(api_token=token)

        self.model_ref = model_ref
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.dpi = dpi
        self.task_key = task_key
        self.task_value = task_value
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    # --- interne Helfer ---

    def _pil_to_bytes(self, img: Image.Image) -> io.BytesIO:
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        return buf

    def _ocr_image(self, img: Image.Image) -> Dict[str, Any]:
        """
        Ruft DeepSeek-OCR mit Retries auf.
        Gibt bei Erfolg: {"markdown": ...}
        Wirft bei endgültigem Fehlschlag eine RuntimeError.
        """
        buf = self._pil_to_bytes(img)

        last_err: Exception | None = None
        for attempt in range(1, self.max_retries + 1):
            try:
                out = self.client.run(
                    self.model_ref,
                    input={
                        "image": buf,
                        self.task_key: self.task_value,
                        # Optional könntest du hier weitere Parameter setzen,
                        # z.B. "resolution_size": "Gundam (Recommended)",
                    },
                    wait=60,  # max. Wartezeit für den Sync-Call
                )
                return {"markdown": out}
            except (socket.timeout, TimeoutError, OSError, Exception) as e:
                last_err = e
                print(f"[OCR] Versuch {attempt} fehlgeschlagen: {e!r}")
                if attempt < self.max_retries:
                    time.sleep(self.retry_delay * attempt)

        raise RuntimeError("DeepSeek-OCR endgültig fehlgeschlagen") from last_err

  

    def process_pdf(self, pdf_path: Path) -> PDFDocumentOutput:
        """
        PDF -> pdf2image -> DeepSeek-OCR
        Speichert Seiten flach als <pdf_stem>__page_001.md/.json in output_dir.
        """
        pdf_path = Path(pdf_path)
        assert pdf_path.is_file(), f"PDF not found: {pdf_path}"

        out_dir = self.output_dir
        out_dir.mkdir(parents=True, exist_ok=True)

        base = pdf_path.stem  # z.B. "Uebungsblatt_1"

        print(f"[PDF] Konvertiere {pdf_path.name} mit dpi={self.dpi} ...")
        pages = convert_from_path(str(pdf_path), dpi=self.dpi)
        out_pages: List[PDFPageOutput] = []

        for i, pil_img in enumerate(pages, start=1):
            print(f"[PDF] OCR Seite {i}/{len(pages)} von {pdf_path.name} ...")
            raw = self._ocr_image(pil_img)

            md = raw.get("markdown", "")
            if isinstance(md, list):
                md = "\n".join(str(x) for x in md)
            md = str(md).strip()

            md_path = out_dir / f"{base}__page_{i:03d}.md"
            json_path = out_dir / f"{base}__page_{i:03d}.json"

            md_path.write_text(md, encoding="utf-8")
            json_path.write_text(json.dumps(raw, indent=2), encoding="utf-8")

            out_pages.append(
                PDFPageOutput(page_number=i, markdown=md, raw_page_json=raw)
            )

        print(f"[PDF] Fertig: {pdf_path.name} -> {len(out_pages)} Seiten")
        return PDFDocumentOutput(file_name=pdf_path.stem, pages=out_pages)

    def process_image_file(self, img_path: Path) -> PDFDocumentOutput:
        """
        Einzelnes Bild (z.B. JPG) -> DeepSeek-OCR.
        Speichert Ergebnis flach als <stem>__page_001.md/.json in output_dir.
        """
        img_path = Path(img_path)
        assert img_path.is_file(), f"Image not found: {img_path}"

        out_dir = self.output_dir
        out_dir.mkdir(parents=True, exist_ok=True)

        img = Image.open(img_path).convert("RGB")

        print(f"[IMG] OCR {img_path.name} ...")
        raw = self._ocr_image(img)

        md = raw.get("markdown", "")
        if isinstance(md, list):
            md = "\n".join(str(x) for x in md)
        md = str(md).strip()

        stem = img_path.stem
        md_path = out_dir / f"{stem}__page_001.md"
        json_path = out_dir / f"{stem}__page_001.json"

        md_path.write_text(md, encoding="utf-8")
        json_path.write_text(json.dumps(raw, indent=2), encoding="utf-8")

        page = PDFPageOutput(page_number=1, markdown=md, raw_page_json=raw)
        return PDFDocumentOutput(file_name=img_path.stem, pages=[page])


# ---------------- CLI-Teil ----------------


def find_pdfs(pdf_root: Path, recursive: bool = False) -> List[Path]:
    pdf_root = Path(pdf_root)
    assert pdf_root.is_dir(), f"PDF-Verzeichnis nicht gefunden: {pdf_root}"

    if recursive:
        files = sorted(pdf_root.rglob("*.pdf"))
    else:
        files = sorted(pdf_root.glob("*.pdf"))

    return files


def main() -> None:
    parser = argparse.ArgumentParser(
        description="OCR für Übungsblatt-PDFs mit DeepSeek-OCR (Replicate)."
    )
    parser.add_argument(
        "--pdf-dir",
        type=str,
        required=True,
        help="Ordner mit Übungsblatt-PDFs (z.B. .../input_data/lösungen/analysis/s3)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        required=True,
        help="Zielordner für Markdown/JSON (z.B. .../data_processed/ANA/3)",
    )
    parser.add_argument(
        "--model-ref",
        type=str,
        default="lucataco/deepseek-ocr:cb3b474fbfc56b1664c8c7841550bccecbe7b74c30e45ce938ffca1180b4dff5",
        help="Replicate Model Ref für DeepSeek-OCR.",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=220,
        help="DPI für pdf2image (Standard: 220).",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Anzahl Wiederholungen pro Seite bei OCR-Fehlern.",
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=5.0,
        help="Basiswartezeit (Sekunden) zwischen Retries.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="PDFs rekursiv im Unterordnern suchen.",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="PDF überspringen, wenn page_001.md bereits existiert.",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=1.0,
        help="Pause (Sekunden) zwischen PDFs zur Entlastung der API.",
    )

    args = parser.parse_args()

    pdf_dir = Path(args.pdf_dir)
    output_dir = Path(args.output_dir)

    print(f"PDF-Verzeichnis:   {pdf_dir}")
    print(f"Output-Verzeichnis:{output_dir}")
    print(f"Modell:            {args.model_ref}")
    print(f"DPI:               {args.dpi}")
    print(f"Retries:           {args.max_retries}, Delay: {args.retry_delay}s")
    print()

    processor = DeepSeekOCRProcessorReplicate(
        model_ref=args.model_ref,
        output_dir=output_dir,
        dpi=args.dpi,
        max_retries=args.max_retries,
        retry_delay=args.retry_delay,
    )

    pdf_files = find_pdfs(pdf_dir, recursive=args.recursive)
    if not pdf_files:
        print("Keine PDFs gefunden.")
        return

    print(f"Gefundene PDFs: {len(pdf_files)}\n")

    for pdf in pdf_files:
        base = pdf.stem
        first_page_md = output_dir / f"{base}__page_001.md"

        if args.skip_existing and first_page_md.is_file():
            print(f"[SKIP] {pdf.name} (bereits verarbeitet)")
            continue

        print(f"=== Verarbeite: {pdf.name} ===")
        try:
            doc = processor.process_pdf(pdf)
            print(f"--> {len(doc.pages)} Seiten erfolgreich verarbeitet.\n")
        except Exception as e:
            print(f"!! Fehler bei {pdf.name}: {e!r}\n")

        time.sleep(args.sleep)


if __name__ == "__main__":
    main()
