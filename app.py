import streamlit as st
import requests

st.title("Agentic AI Legal Assistant (India)")

st.write("Ask any legal question related to BSA, BNS, or legal terms:")

question = st.text_area("Your Question:")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = requests.post(
            "http://localhost:5001/ask",
            json={"question": question}
        )
        if response.status_code == 200:
            answer = response.json()["answer"]
            st.success("AI Answer:")
            st.write(answer)
        else:
            st.error("Error getting response from AI backend.")
