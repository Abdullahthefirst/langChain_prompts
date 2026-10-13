from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
chat_history = [
    SystemMessage(content="You are a helpful AI assistant")
]

# Now adding all chat_history in a single list can be messy, rather we create a list of lists

while(True):
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if(user_input.lower() == "exit"): #enter "exit" to leave
        break
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)
#the above all can be done by langchain classes i.e. by distinct role of system, human, and AI message