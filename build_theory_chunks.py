#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


def build_theory_chunks_from_files(md_paths: List[Path], course: str) -> List[Document]:
    """
    Nimmt eine oder mehrere Theorie-Markdown-Dateien (bereits 'clean'),
    splittet sie:
      - nach H1–H4-Überschriften
      - dann rekursiv in Chunks
    und hängt Metadaten wie course, type, heading, source, chunk_id an.
    """
    headers_to_split_on = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3"),
        ("####", "h4"),
    ]

    md_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=True,   
    )

    char_splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=80,
        separators=["\n## ", "\n### ", "\n", " ", ""],
        add_start_index=True,
    )

    all_chunks: List[Document] = []

    for md_path in md_paths:
        print(f"\nLade Theorie-Datei: {md_path}")
        docs = TextLoader(str(md_path), encoding="utf-8").load()
        base_doc = docs[0]
        text = base_doc.page_content

        # 1) Section-Split per Markdown-Header
        section_docs = md_splitter.split_text(text)

        # Basis-Metadaten an jede Section hängen
        for d in section_docs:
            d.metadata.update({
                "source": md_path.name,
                "course": course,
                "type": "theory",
            })
            # Überschrift aus h1/h2/h3 zusammenbauen
            h1 = d.metadata.get("h1")
            h2 = d.metadata.get("h2")
            h3 = d.metadata.get("h3")
            heading_parts = [x for x in (h1, h2, h3) if x]
            if heading_parts:
                d.metadata["heading"] = " – ".join(heading_parts)

        # 2) Feinschnitt in Chunks
        chunk_docs = char_splitter.split_documents(section_docs)
        print(f"  Sections: {len(section_docs)}, Chunks: {len(chunk_docs)}")

        all_chunks.extend(chunk_docs)

    # 3) Globale chunk_id vergeben
    for i, d in enumerate(all_chunks, start=1):
        d.metadata["chunk_id"] = i

    print(f"\nGESAMT: {len(all_chunks)} Theorie-Chunks über {len(md_paths)} Datei(en).")
    return all_chunks


def export_chunks_jsonl(chunks: List[Document], jsonl_path: Path) -> None:
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    with jsonl_path.open("w", encoding="utf-8") as f:
        for d in chunks:
            rec = {
                "content": d.page_content,
                "metadata": d.metadata,
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("Chunks als JSONL exportiert nach:", jsonl_path)


def build_chroma_for_theory(
    chunks: List[Document],
    embed_model: str,
    chroma_dir: Path,
    collection_name: str,
) -> None:
    print("\nBaue Chroma-Vektorstore für Theorie ...")

    embedder = OllamaEmbeddings(
        model=embed_model,
     
    )

    chroma_dir.mkdir(parents=True, exist_ok=True)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedder,
        persist_directory=str(chroma_dir),
        collection_name=collection_name,
        collection_metadata={"hnsw:space": "cosine"},
    )

  
    print("Chroma-Vektorstore gespeichert in:", chroma_dir)
    print("Collection-Name:", collection_name)


def main():
    parser = argparse.ArgumentParser(
        description="Baue Theorie-Chunks (und optional Chroma) aus einer oder mehreren Markdown-Dateien."
    )
    parser.add_argument(
        "--md-path",
        type=str,
        nargs="+",
        required=True,
        help="Eine oder mehrere 'full_clean' Markdown-Dateien für die Theorie.",
    )
    parser.add_argument(
        "--course",
        type=str,
        required=True,
        help="Kursname, z.B. 'Analysis1', 'Analysis2', 'LA1', ...",
    )
    parser.add_argument(
        "--jsonl-out",
        type=str,
        default=None,
        help="Pfad für den JSONL-Export der Chunks. Wenn leer, wird im Ordner der ersten MD-Datei gespeichert.",
    )
    parser.add_argument(
        "--use-chroma",
        action="store_true",
        help="Wenn gesetzt, wird ein Chroma-Vektorstore gebaut.",
    )
    parser.add_argument(
        "--chroma-dir",
        type=str,
        default=None,
        help="Verzeichnis für den Chroma-Vektorstore.",
    )
    parser.add_argument(
        "--collection-name",
        type=str,
        default=None,
        help="Name der Chroma-Collection (Standard: <course>_theory, klein geschrieben).",
    )
    parser.add_argument(
        "--embed-model",
        type=str,
        default="mxbai-embed-large",
        help="Ollama-Embedding-Modell (Standard: mxbai-embed-large).",
    )

    args = parser.parse_args()

    md_paths = [Path(p) for p in args.md_path]
    for p in md_paths:
        if not p.is_file():
            raise FileNotFoundError(f"Markdown-Datei nicht gefunden: {p}")

    course = args.course

    # Chunks bauen
    theory_chunks = build_theory_chunks_from_files(md_paths, course=course)

    # JSONL-Pfad bestimmen
    if args.jsonl_out is not None:
        jsonl_path = Path(args.jsonl_out)
    else:
        
        jsonl_path = md_paths[0].parent / f"Theorie_{course}_chunks.jsonl"

    export_chunks_jsonl(theory_chunks, jsonl_path)

   
    if args.use_chroma:
        if args.chroma_dir is not None:
            chroma_dir = Path(args.chroma_dir)
        else:
            
            chroma_dir = Path("vectorstore") / f"{course.lower()}_theory"

        collection_name = args.collection_name or f"{course.lower()}_theory"

        build_chroma_for_theory(
            theory_chunks,
            embed_model=args.embed_model,
            chroma_dir=chroma_dir,
            collection_name=collection_name,
        )


if __name__ == "__main__":
    main()
