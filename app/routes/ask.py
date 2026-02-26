from langchain_community.llms import Ollama

llm = Ollama(model="tinyllama")

def process_question(question: str):
    response = llm.invoke(question)
    return response