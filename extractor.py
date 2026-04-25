# extractor.py
import requests

PROJECT_ID = "bc-game-crashdata"

URL = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents:runQuery"


def fetch(collection="crash", limit=100):
    payload = {
        "structuredQuery": {
            "from": [{"collectionId": collection}],
            "limit": limit
        }
    }

    r = requests.post(URL, json=payload)
    return r.json()
