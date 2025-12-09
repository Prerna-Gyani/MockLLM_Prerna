import streamlit as st
from openai import OpenAI

st.title("Mock ChatGPT (Streamlit Cloud Compatible)")

BASE_URL = "https://mockllm.anya2a.com/v1"
DUMMY_KEY = "DeepChat"

prompt = st.text_area("Ask something:")

if st.button("Generate Mock Response"):
    try:
        client = OpenAI(
            api_key=DUMMY_KEY,
            base_url=BASE_URL  # <-- This is valid in new SDK
        )

        response = client.chat.completions.create(
            model="mock-gpt",
            messages=[{"role": "user", "content": prompt}]
        )

        st.success(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Error: {e}")
