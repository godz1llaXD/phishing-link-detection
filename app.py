import sys
import os

# Ensure src is importable
sys.path.append(os.path.abspath("."))

import streamlit as st
from src.predict import analyze_url

# ---------------- UI CONFIG ----------------
st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🔐",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("🔐 Phishing URL Detection")
st.markdown("Detect whether a URL is **Phishing** or **Legitimate** using Machine Learning.")

# ---------------- INPUT ----------------
url_input = st.text_input("Enter URL:", placeholder="https://example.com")

# ---------------- BUTTON ----------------
if st.button("Analyze URL"):

    if not url_input:
        st.warning("Please enter a URL")
    
    else:
        with st.spinner("Analyzing..."):
            result = analyze_url(url_input)

        if "error" in result:
            st.error(f"Error: {result['error']}")
        else:
            prediction = result["prediction"]
            confidence = result["probability"]
            reasons = result["reasons"]

            # ---------------- RESULT ----------------
            if prediction == 1:
                st.error("🚨 Phishing URL Detected")
            else:
                st.success("✅ Legitimate URL")

            # Confidence
            st.metric("Confidence Score", f"{confidence * 100:.2f}%")

            # ---------------- REASONS ----------------
            if reasons:
                st.subheader("🔍 Why?")
                for r in reasons:
                    st.write(f"- {r}")
            else:
                st.info("No strong suspicious indicators detected.")