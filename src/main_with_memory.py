from langchain_ollama import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Initialize the chat model
chat_model = ChatOllama(model="hf.co/bartowski/Llama-3.2-3B-Instruct-GGUF:latest")

# Create a conversation chain with memory
conversation = ConversationChain(
    llm=chat_model,
    memory=ConversationBufferMemory()
)

# Have a conversation
response1 = conversation.predict(input="Hi, I'm John. What's your name?")
print(response1)

response2 = conversation.predict(input="What's my name?")
print(response2)