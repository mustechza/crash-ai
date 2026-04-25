# app.py
import streamlit as st
import time
from backend import get_live_data

st.set_page_config(page_title="Crash AI", layout="wide")

st.title("🚀 Crash AI Cloud Predictor")

placeholder = st.empty()

while True:
    df, signal = get_live_data()

    if df is not None:
        with placeholder.container():
            st.line_chart(df["multiplier"])
            st.subheader("Signal")
            st.write(signal)

    time.sleep(3)
