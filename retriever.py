#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import Dict, Any

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.retrievers import EnsembleRetriever
from langchain.schema import BaseRetriever


# =======================
#   KONFIGURATION
# =======================

# Basisordner für deine Text-Vectorstores
BASE_VS_DIR = Path("/Users/thuvarakayograjah/Documents/RAG/R-G-/vectorstore")

# Theorie & Übungs-Vectorstores
# -> Passe die Pfade/Collection-Namen hier an deine existierenden Stores an.
VECTORSTORE_CONFIG: Dict[str, Dict[str, Any]] = {
    # Theorie
    "analysis1_theory": {
        "persist_dir": BASE_VS_DIR / "analysis1_theory",
        "collection": "analysis1_theory",
        "filter": {"type": "theory"},
    },
    "analysis2_theory": {
        "persist_dir": BASE_VS_DIR / "analysis2_theory",
        "collection": "analysis2_theory",
        "filter": {"type": "theory"},
    },
    "analysis3_theory": {
        "persist_dir": BASE_VS_DIR / "analysis3_theory",
        "collection": "analysis3_theory",
        "filter": {"type": "theory"},
    },
    "linearealgebra1_theory": {
        "persist_dir": BASE_VS_DIR / "linearealgebra1_theory",
        "collection": "linearealgebra1_theory",
        "filter": {"type": "theory"},
    },
     "linearealgebra2_theory": {
        "persist_dir": BASE_VS_DIR / "linearealgebra2_theory",
        "collection": "linearealgebra2_theory",
        "filter": {"type": "theory"},
    },
     "stochastik1_theory": {
        "persist_dir": BASE_VS_DIR / "stochastik1_theory",
        "collection": "stochastik1_theory",
        "filter": {"type": "theory"},
    },
    "stochastik3_theory": {
        "persist_dir": BASE_VS_DIR / "stochastik3_theory",
        "collection": "stochastik3_theory",
        "filter": {"type": "theory"},
    },

    # Übungen (hier erstmal nur Analysis 3, weitere kannst du nachrüsten)
    "analysis1_exercise": {
        "persist_dir": BASE_VS_DIR / "analysis1_exercise",
        "collection": "analysis1_exercise",
        "filter": {"type": "exercise"},
    },
    "analysis2_exercise": {
        "persist_dir": BASE_VS_DIR / "analysis2_exercise",
        "collection": "analysis2_exercise",
        "filter": {"type": "exercise"},
    },
    "analysis3_exercise": {
        "persist_dir": BASE_VS_DIR / "analysis3_exercise",
        "collection": "analysis3_exercise",
        "filter": {"type": "exercise"},
    },
    "linearealgebra1_exercise": {
        "persist_dir": BASE_VS_DIR / "linearealgebra1_exercise",
        "collection": "linearealgebra1_exercise",
        "filter": {"type": "exercise"},
    },
     "linearealgebra2_exercise": {
        "persist_dir": BASE_VS_DIR / "linearealgebra2_exercise",
        "collection": "linearealgebra2_exercise",
        "filter": {"type": "exercise"},
    },
     "stochastik1_exercise": {
        "persist_dir": BASE_VS_DIR / "stochastik1_exercise",
        "collection": "stochastik1_exercise",
        "filter": {"type": "exercise"},
    },
    "stochastik3_exercise": {
        "persist_dir": BASE_VS_DIR / "stochastik3_exercise",
        "collection": "stochastik3_exercise",
        "filter": {"type": "exercise"},
    },
}



# Bild-Vectorstore (Text-Embeddings der Bilder, die du gerade gebaut hast)
IMAGE_VS_DIR = Path(
    "/Users/thuvarakayograjah/Documents/RAG/R-G-/vectorstore/theory_images_text"
)
IMAGE_COLLECTION = "analysis3_images_text"

# Root-Ordner, relativ zu dem die Bildpfade im Metadata-Feld "path" angegeben sind
IMAGE_ROOT = Path("/Users/thuvarakayograjah/Documents/RAG/R-G-/input_data")

# Embedding-Modell in Ollama
EMBED_MODEL = "mxbai-embed-large"  # muss in Ollama verfügbar sein


# =======================
#   HILFSFUNKTIONEN
# =======================

def get_embedder() -> OllamaEmbeddings:
    """
    Einheitlicher Embedder für alle Vectorstores (Text & Bilder).
    """
    return OllamaEmbeddings(
        model=EMBED_MODEL,
        # base_url="http://localhost:11434",  # falls dein Ollama woanders läuft
    )


def load_chroma(key: str) -> Chroma:
    """
    Lädt einen bestehenden Chroma-Vectorstore basierend auf dem key,
    z.B. 'analysis3_theory' oder 'analysis3_exercises'.
    """
    if key not in VECTORSTORE_CONFIG:
        raise KeyError(f"Unbekannter Vectorstore-Key: {key!r}")

    cfg = VECTORSTORE_CONFIG[key]
    persist_dir: Path = cfg["persist_dir"]
    collection_name: str = cfg["collection"]

    if not persist_dir.exists():
        raise FileNotFoundError(
            f"Persist-Directory für '{key}' nicht gefunden: {persist_dir}"
        )

    embedder = get_embedder()

    db = Chroma(
        collection_name=collection_name,
        embedding_function=embedder,
        persist_directory=str(persist_dir),
    )
    return db


def get_retriever(key: str, k: int = 5) -> BaseRetriever:
    """
    Baut einen Retriever für einen einzelnen Vectorstore anhand des CONFIG-Keys.
    """
    db = load_chroma(key)
    cfg = VECTORSTORE_CONFIG[key]
    flt = cfg.get("filter") or {}

    retriever = db.as_retriever(
        search_kwargs={
            "k": k,
            "filter": flt,
        }
    )
    return retriever


def get_theory_retriever(course: str, k: int = 5) -> BaseRetriever:
    """
    Retriever nur für die Theorie eines Kurses.
    course: "Analysis1", "Analysis2", "Analysis3"
    """
    key = f"{course.lower()}_theory"
    return get_retriever(key, k=k)


def get_exercise_retriever(course: str, k: int = 5) -> BaseRetriever:
    """
    Retriever nur für Übungen eines Kurses.
    (Vectorstore muss dafür in VECTORSTORE_CONFIG eingetragen sein.)
    """
    key = f"{course.lower()}_exercises"
    return get_retriever(key, k=k)


def get_combined_retriever(
    course: str,
    k_theory: int = 4,
    k_exercises: int = 4,
    w_theory: float = 0.6,
    w_exercises: float = 0.4,
) -> BaseRetriever:
    """
    Kombinierter Retriever (Theorie + Übungen) mit EnsembleRetriever.

    - course: "Analysis1" | "Analysis2" | "Analysis3"
    - k_theory: Anzahl Theorie-Chunks
    - k_exercises: Anzahl Übungs-Chunks
    - w_theory, w_exercises: Gewichte (werden intern normalisiert)
    """
    course_norm = course.lower()

    key_theory = f"{course_norm}_theory"
    key_ex = f"{course_norm}_exercises"

    retr_theory = get_retriever(key_theory, k=k_theory)
    retr_ex = get_retriever(key_ex, k=k_exercises)

    ensemble = EnsembleRetriever(
        retrievers=[retr_theory, retr_ex],
        weights=[w_theory, w_exercises],
    )
    return ensemble


def get_image_retriever(k: int = 8) -> BaseRetriever:
    """
    Retriever für deinen Bild-Vectorstore (theory_images_text).

    Achtung: Hier nutzen wir die Text-Embeddings der Bild-Summaries,
    d.h. du kannst mit Textfragen nach passenden Bildern suchen.
    """
    embedder = get_embedder()

    if not IMAGE_VS_DIR.exists():
        raise FileNotFoundError(
            f"Image-Vectorstore-Verzeichnis nicht gefunden: {IMAGE_VS_DIR}"
        )

    db = Chroma(
        collection_name=IMAGE_COLLECTION,
        embedding_function=embedder,
        persist_directory=str(IMAGE_VS_DIR),
    )

    # Falls du bei den Bild-Metadaten "type": "image" gesetzt hast,
    # kannst du hier noch filter={"type": "image"} ergänzen.
    retriever = db.as_retriever(
        search_kwargs={
            "k": k,
            # "filter": {"type": "image"},
        }
    )
    return retriever


# =======================
#   SELF-TEST
# =======================

if __name__ == "__main__":
    # --- Test 1: Theory-Retriever ---
    print("=== TEST: Analysis3 Theorie ===")
    try:
        r_theory = get_theory_retriever("Analysis3", k=3)
        docs_t = r_theory.get_relevant_documents("Was ist die Produktregel?")
        for i, d in enumerate(docs_t, 1):
            m = d.metadata
            print(f"[{i}] type={m.get('type')} source={m.get('source')} chunk_id={m.get('chunk_id')}")
            print(d.page_content[:200].replace("\n", " "), "...\n")
    except Exception as e:
        print("Fehler beim Theorie-Retriever:", e)

    # --- Test 2: Exercises-Retriever ---
    print("=== TEST: Analysis3 Übungen ===")
    try:
        r_ex = get_exercise_retriever("Analysis3", k=3)
        docs_e = r_ex.get_relevant_documents("Aufgabe zur Kettenregel")
        for i, d in enumerate(docs_e, 1):
            m = d.metadata
            print(f"[{i}] type={m.get('type')} source={m.get('source')} chunk_id={m.get('chunk_id')}")
            print(d.page_content[:200].replace("\n", " "), "...\n")
    except Exception as e:
        print("Fehler beim Übungs-Retriever:", e)

    # --- Test 3: Kombiniert Theorie + Übungen ---
    print("=== TEST: Kombinierter Retriever (Analysis3) ===")
    try:
        r_combo = get_combined_retriever("Analysis3", k_theory=3, k_exercises=3)
        docs_c = r_combo.get_relevant_documents(
            "Erkläre die Produktregel und gib eine Beispielaufgabe dazu."
        )
        for i, d in enumerate(docs_c, 1):
            m = d.metadata
            print(f"[{i}] type={m.get('type')} source={m.get('source')} chunk_id={m.get('chunk_id')}")
            print(d.page_content[:200].replace("\n", " "), "...\n")
    except Exception as e:
        print("Fehler beim kombinierten Retriever:", e)

    # --- Test 4: Bild-Retriever ---
    print("=== TEST: Bild-Retriever (analysis3_images_text) ===")
    try:
        r_img = get_image_retriever(k=4)
        docs_img = r_img.get_relevant_documents("Integralaufgabe mit bestimmtem Integral")
        for i, d in enumerate(docs_img, 1):
            m = d.metadata
            rel_path = m.get("path")
            filename = m.get("filename")
            summary = m.get("summary")
            full_path = (IMAGE_ROOT / rel_path).resolve() if rel_path else None

            print(f"[{i}] {filename}")
            print("   summary:", summary)
            print("   rel path:", rel_path)
            print("   full path:", full_path)
            print()
    except Exception as e:
        print("Fehler beim Bild-Retriever:", e)
