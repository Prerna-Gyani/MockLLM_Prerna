import streamlit as st

st.title("Simulated MockLLM Demo (Streamlit Cloud)")

prompt = st.text_area("Ask something:")

mock_responses = {
    "Hello": "Hi there! How can I help you today?",
    "Tell me a joke": "Why did the computer go to the doctor? Because it caught a virus!"
}

if st.button("Generate"):
    output = mock_responses.get(prompt, "Sorry, I don't know the answer to that.")
    st.success(output)
