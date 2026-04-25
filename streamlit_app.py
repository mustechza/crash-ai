import streamlit as st
import pandas as pd
from model import predict
from features import build_features

st.title("🚀 Crash AI Predictor")

df = pd.read_csv("crash_dataset.csv")

df = build_features(df)

st.line_chart(df["multiplier"])

latest = df.iloc[-1]

st.subheader("Latest Signal")
st.write(predict(latest))
