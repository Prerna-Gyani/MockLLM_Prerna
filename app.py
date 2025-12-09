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

        # Safely extract text
        output = ""
        if "choices" in result and len(result["choices"]) > 0:
            if "message" in result["choices"][0]:
                output = result["choices"][0]["message"].get("content", "")
            elif "text" in result["choices"][0]:  # fallback for some mock responses
                output = result["choices"][0]["text"]

        if output:
            st.success(output)
        else:
            st.warning("No content returned from the mock API.")

    except Exception as e:
        st.error(f"Error: {e}")
