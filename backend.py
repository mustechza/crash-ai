# backend.py
import time
import pandas as pd
from extractor import fetch
from parser import parse
from features import build
from model import predict

buffer = []

def get_live_data():
    data = fetch()

    for item in data:
        parsed = parse(item)
        if parsed:
            buffer.append(parsed)

    if len(buffer) < 30:
        return None, None

    df = pd.DataFrame(buffer[-200:])
    df = build(df)

    latest = df.iloc[-1]

    signal = predict(latest)

    return df, signal
