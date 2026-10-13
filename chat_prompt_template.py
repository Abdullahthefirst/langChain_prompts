from langchain_core.prompts import ChatPromptTemplate

#Using ChatPromptTemplate.from_messages() works the same way

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])
#working of chatPromptTemplate class is kind of different from PromptTemplate class
prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Dusra'})

print(prompt)