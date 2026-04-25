
import time
import pandas as pd
from extractor import fetch
from parser import parse
from features import build_features
from model import predict

buffer = []

def run():
    while True:
        data = fetch()

        for item in data:
            parsed = parse(item)
            if parsed:
                buffer.append(parsed)

        if len(buffer) < 30:
            print("Collecting data...")
            time.sleep(3)
            continue

        df = pd.DataFrame(buffer[-200:])
        df = build_features(df)

        latest = df.iloc[-1]

        signal = predict(latest)

        print(f"Multiplier: {latest['multiplier']} | Signal: {signal}")

        time.sleep(3)

if __name__ == "__main__":
    run()
