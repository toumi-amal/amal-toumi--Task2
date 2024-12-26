import streamlit as st
from main import find_similar_question

# Simple Streamlit interface
st.title("Python FAQ Retrieval System")

st.write("Ask your question below:")

# User input for the question
user_question = st.text_input("Enter your question:")


# Display the result when the user submits a question
if user_question:
    similar_question, answer = find_similar_question(user_question)
    
    st.write(f"**Your Question:** {user_question}")
    st.write(f"**Most Similar Question:** {similar_question}")
    st.write(f"**Answer:** {answer}")
