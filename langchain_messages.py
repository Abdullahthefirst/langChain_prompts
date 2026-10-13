from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
#System message is defined in start by the user like 
#   you are an assistant. Answer quries respectfully

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about LangChain"),
]
# print(messages)

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(result.content)
