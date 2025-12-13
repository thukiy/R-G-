#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Any

import chromadb
from tqdm import tqdm
from langchain_ollama import OllamaEmbeddings



JSON_IN = Path("/Users/thuvarakayograjah/Documents/RAG/R-G-/image_embeddings.json")
JSON_OUT = Path("/Users/thuvarakayograjah/Documents/RAG/R-G-/images_analysis3_text_emb.json")


CHROMA_PATH = Path("/Users/thuvarakayograjah/Documents/RAG/R-G-/vectorstore/theory_images_text")
CHROMA_COLLECTION = "analysis3_images_text"

# Text-Embedding Modell (Ollama)
TEXT_EMB_MODEL = "mxbai-embed-large"


def load_records(json_path: Path) -> List[Dict[str, Any]]:
    data = json.loads(json_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Erwarte eine Liste von Records im JSON.")
    return data


def build_text_embeddings(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Nimmt deine vorhandenen Bild-Records (mit embedding=None)
    und erzeugt Text-Embeddings auf Basis von summary/filename/path.
    """
    embedder = OllamaEmbeddings(model=TEXT_EMB_MODEL)

    updated: List[Dict[str, Any]] = []

    for i, rec in enumerate(tqdm(records, desc="Text-Embeddings für Bilder")):
        meta = rec.get("metadata") or {}

        # 1) Textbasis für das Embedding wählen
        summary = (meta.get("summary") or "").strip()
        if not summary:
            
            filename = meta.get("filename") or ""
            path = meta.get("path") or ""
            fallback = filename or path or "Mathe Skript Bild"
            summary = fallback
            meta["summary"] = summary  

        try:
            text_emb = embedder.embed_query(summary)
        except Exception as e:
            print(f"⚠️  Record {i}: Fehler beim Text-Embedding für '{summary[:60]}...': {e}")
            continue

        rec["embedding"] = text_emb
        rec["metadata"] = meta
        updated.append(rec)

    print(f"Records total: {len(records)}, mit Text-Embedding: {len(updated)}")
    return updated


def save_in_chroma(records: List[Dict[str, Any]]) -> None:
    CHROMA_PATH.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    collection = client.get_or_create_collection(CHROMA_COLLECTION)

    ids, embeddings, metadatas, documents = [], [], [], []
    dim = None
    kept = 0
    skipped = 0

    for i, rec in enumerate(records):
        emb = rec.get("embedding")
        meta = rec.get("metadata") or {}

        if emb is None or not isinstance(emb, (list, tuple)) or len(emb) == 0:
            skipped += 1
            continue

        if dim is None:
            dim = len(emb)
        elif len(emb) != dim:
            print(f"⚠️  Record {i}: Embedding-Dimension inkonsistent, skip.")
            skipped += 1
            continue

        ids.append(f"img-{i:06d}")
        embeddings.append(list(emb))
        metadatas.append(meta)
        documents.append(meta.get("summary") or meta.get("filename") or "")

        kept += 1

    if not embeddings:
        print("⚠️  Keine gültigen Embeddings – nichts in Chroma gespeichert.")
        return

    collection.add(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas,
        documents=documents,
    )

    print(f"Chroma: {kept} Bilder gespeichert, {skipped} übersprungen.")
    print("Collection:", CHROMA_COLLECTION)
    print("Pfad:", CHROMA_PATH)


def main():
    if not JSON_IN.is_file():
        raise FileNotFoundError(f"JSON nicht gefunden: {JSON_IN}")

    records = load_records(JSON_IN)
    print("Records im JSON:", len(records))

    rebuilt = build_text_embeddings(records)

    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(rebuilt, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Neues JSON mit Text-Embeddings:", JSON_OUT)

    save_in_chroma(rebuilt)


if __name__ == "__main__":
    main()
