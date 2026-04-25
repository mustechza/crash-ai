import requests

PROJECT_ID = "bc-game-crashdata"

BASE_URL = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents:runQuery"

def fetch(collection="crash", limit=50):
    payload = {
        "structuredQuery": {
            "from": [{"collectionId": collection}],
            "limit": limit
        }
    }

    r = requests.post(BASE_URL, json=payload)
    return r.json()
