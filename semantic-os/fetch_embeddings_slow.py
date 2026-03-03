#!/usr/bin/env python3
"""
Pomocniczy skrypt do pobierania embeddingów partiami z pauzą 65s między batchami.
Zapisuje do cache: data/embeddings/kosze_prezentowe_cache.json
"""
import json
import time
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

import pandas as pd
from google import genai

EMBEDDING_MODEL = "gemini-embedding-001"
CACHE_PATH = Path("D:/SensAI 3.0/semantic-os-audyt/semantic-os/data/embeddings/kosze_prezentowe_cache.json")
INPUT_CSV = Path("D:/SensAI 3.0/semantic-os-audyt/semantic-os/data/keywords/kosze_prezentowe_expanded.csv")
BATCH_SIZE = 100
PAUSE_BETWEEN_BATCHES = 65  # seconds

import os
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment")

client = genai.Client(api_key=api_key)

# Wczytaj CSV
df = pd.read_csv(INPUT_CSV)
keywords = [kw.strip().lower() for kw in df["keyword"].tolist() if isinstance(kw, str) and kw.strip()]
keywords = list(dict.fromkeys(keywords))  # deduplikacja
print(f"Total keywords: {len(keywords)}")

# Wczytaj istniejacy cache
cache = {}
if CACHE_PATH.exists():
    with open(CACHE_PATH, "r", encoding="utf-8") as f:
        cache = json.load(f)
    print(f"Cache wczytany: {len(cache)} embeddingow")

# Filtruj tylko brakujace
new_keywords = [kw for kw in keywords if kw not in cache]
print(f"Do pobrania: {len(new_keywords)} keywords")

if not new_keywords:
    print("Wszystkie embeddingi juz w cache!")
else:
    for i in range(0, len(new_keywords), BATCH_SIZE):
        batch = new_keywords[i:i + BATCH_SIZE]
        print(f"\nBatch {i//BATCH_SIZE + 1}: keywords {i+1}-{min(i+BATCH_SIZE, len(new_keywords))}/{len(new_keywords)}...")

        for attempt in range(3):
            try:
                result = client.models.embed_content(
                    model=EMBEDDING_MODEL,
                    contents=batch,
                    config={"task_type": "CLUSTERING"},
                )
                for kw, embedding in zip(batch, result.embeddings):
                    cache[kw] = list(embedding.values)
                print(f"  OK - pobrano {len(batch)} embeddingow")
                break
            except Exception as e:
                print(f"  Attempt {attempt+1}/3 failed: {e}")
                if attempt < 2:
                    time.sleep(10)
                else:
                    print("  Zapisuje cache i przerywam...")
                    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
                    with open(CACHE_PATH, "w", encoding="utf-8") as f:
                        json.dump(cache, f, ensure_ascii=False)
                    raise

        # Zapisz po kazdym batchu
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(CACHE_PATH, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False)
        print(f"  Cache zapisany: {len(cache)} embeddingow total")

        # Przerwa przed nastepnym batchem (jesli jest)
        if i + BATCH_SIZE < len(new_keywords):
            remaining = len(new_keywords) - (i + BATCH_SIZE)
            print(f"  Czekam {PAUSE_BETWEEN_BATCHES}s przed kolejnym batchem ({remaining} keywords pozostalo)...")
            time.sleep(PAUSE_BETWEEN_BATCHES)

print(f"\nGotowe! Cache zawiera {len(cache)} embeddingow.")
