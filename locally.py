# app.py
import streamlit as st
import requests

st.title("MockLLM + Streamlit Demo")

# If you run MockLLM locally:
BASE_URL = "http://localhost:8000/v1/chat/completions"

prompt = st.text_area("Your prompt:")

if st.button("Generate"):
    data = {
        "model": "mock-llm",
        "messages": [{"role": "user", "content": prompt}]
    }
    resp = requests.post(BASE_URL, json=data, headers={"Content-Type": "application/json"})
    result = resp.json()
    if "choices" in result and result["choices"]:
        assistant_msg = result["choices"][0]["message"]["content"]
        st.success(assistant_msg)
    else:
        st.error("No valid response from MockLLM")
