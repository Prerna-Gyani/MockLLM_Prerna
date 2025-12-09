import streamlit as st
import requests

st.title("Mock ChatGPT (Streamlit Cloud Compatible)")

BASE_URL = "https://mockllm.anya2a.com/v1/chat/completions"
DUMMY_KEY = "DeepChat"

prompt = st.text_area("Ask something:")

if st.button("Generate Mock Response"):
    try:
        headers = {
            "Authorization": f"Bearer {DUMMY_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "mock-gpt",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(BASE_URL, headers=headers, json=data)

        result = response.json()

        # Extract text like normal OpenAI result
        output = result["choices"][0]["message"]["content"]

        st.success(output)

    except Exception as e:
        st.error(f"Error: {e}")
