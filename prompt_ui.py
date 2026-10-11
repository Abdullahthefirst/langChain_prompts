from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


import streamlit as st
load_dotenv()

model = ChatOpenAI(model='gpt-6-luna')

load_dotenv()
st.header("Research")
user_input = st.text_input("Enter your prompt")
if st.button("Summarize"):
    result = model.invoke(user_input)
    st.subheader("Result")
    st.write(result.content)

