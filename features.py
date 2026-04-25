# features.py
import pandas as pd

def build(df):
    df = df.sort_values("timestamp")

    df["ma5"] = df["multiplier"].rolling(5).mean()
    df["ma10"] = df["multiplier"].rolling(10).mean()
    df["volatility"] = df["multiplier"].rolling(10).std()

    df["momentum"] = df["multiplier"].diff()

    df["low_streak"] = (df["multiplier"] < 2).astype(int).rolling(5).sum()

    return df.dropna()
