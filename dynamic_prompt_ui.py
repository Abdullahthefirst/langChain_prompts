from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv


import streamlit as st
load_dotenv()

model = ChatOpenAI(model='gpt-6-luna')

load_dotenv()
st.header("Research")
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Select...",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)  #[cite: 1]

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)  #[cite: 1]

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)  #[cite: 1]
template = load_prompt('template.json')  #[cite: 2]
formatted_prompt = template.invoke({
    'paper_input':paper_input, 
    'style_input':style_input, 
    'length_input':length_input
})
if st.button("Summarize"):
    response = model.invoke(formatted_prompt)
    st.write(response.content)

