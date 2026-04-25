
import pandas as pd

def build_features(df):
    df = df.sort_values("timestamp")

    df["ma_5"] = df["multiplier"].rolling(5).mean()
    df["ma_10"] = df["multiplier"].rolling(10).mean()

    df["volatility"] = df["multiplier"].rolling(10).std()

    df["momentum"] = df["multiplier"] - df["multiplier"].shift(1)

    df["low_streak"] = (df["multiplier"] < 2).astype(int).rolling(5).sum()

    return df.dropna()
