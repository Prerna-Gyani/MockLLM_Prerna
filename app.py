import streamlit as st
from openai import OpenAI

st.title("Mock ChatGPT (Works on Streamlit Cloud Without API Key)")

# Public mock OpenAI server
BASE_URL = "https://mockllm.anya2a.com/v1"
DUMMY_KEY = "DeepChat"  # Public dummy key accepted by mock API

prompt = st.text_area("Ask something:")

if st.button("Generate Mock Response"):
    try:
        client = OpenAI(
            api_key=DUMMY_KEY,
            base_url=BASE_URL
        )

        response = client.chat.completions.create(
            model="mock-gpt",
            messages=[{"role": "user", "content": prompt}]
        )

        st.success(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Error: {e}")
