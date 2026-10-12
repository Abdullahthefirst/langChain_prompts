from langchain_core.prompts import PromptTemplate, load_prompt

template = PromptTemplate(
    template="""Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
    - Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length. As for the mathematical details, they should be in a format that st.write() function of streamlit library detects them to be written in mathematical symbols""", input_variables=['paper_input', 'style_input', 'length_input']
) 
template.save('template.json')
#in other file you can use the load_prompt() function to get the prompt as reused by action like
#template = load_prompt('template.json')