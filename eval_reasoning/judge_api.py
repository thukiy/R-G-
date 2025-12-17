# judge_api.py
from typing import List, Dict
from openai import OpenAI, RateLimitError
import os
import time
from dotenv import load_dotenv

# .env laden (NOVITA_API_KEY=...)
load_dotenv()

API_KEY = os.getenv("NOVITA_API_KEY")
if API_KEY is None:
    raise RuntimeError("NOVITA_API_KEY ist nicht gesetzt. Bitte in .env definieren.")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.novita.ai/openai",
)


def call_judge_model_novita(messages: List[Dict[str, str]]) -> str:
    """
    Ruft den Judge (Qwen 2.5 72B) über Novita auf,
    mit einfacher Retry-Logik bei RateLimitError.
    """
    max_retries = 5
    backoff_seconds = 10  # im Zweifel höher setzen

    for attempt in range(1, max_retries + 1):
        try:
            print(f"[judge_api] Request an Judge (Versuch {attempt}/{max_retries})...")
            response = client.chat.completions.create(
                model="qwen/qwen3-vl-235b-a22b-thinking",
                messages=messages,
                max_tokens=2048,
                temperature=0.0,
            )
            return response.choices[0].message.content

        except RateLimitError as e:
            print(f"[judge_api] RateLimitError: {e}")
            if attempt == max_retries:
                print("[judge_api] Max. Anzahl Retries erreicht, breche ab.")
                raise
            print(f"[judge_api] Warten {backoff_seconds} Sekunden und nochmal versuchen...")
            time.sleep(backoff_seconds)

        except Exception as e:
            print("[judge_api] Unerwarteter Fehler:", repr(e))
            raise


if __name__ == "__main__":
    # Mini-Test
    test_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Sag mir einen sehr kurzen Witz auf Deutsch."}
    ]
    out = call_judge_model_novita(test_messages)
    print("Antwort:")
    print(out)
