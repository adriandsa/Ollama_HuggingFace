from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the Ollama model
llm = OllamaLLM(model="hf.co/bartowski/Llama-3.2-3B-Instruct-GGUF:latest")

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question: {question}"
)

# Create an LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Use the chain to generate a response
response = chain.run("What is the capital of France?")
print(response)