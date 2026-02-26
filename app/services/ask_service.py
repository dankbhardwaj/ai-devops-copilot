from langchain_ollama import OllamaLLM
from app.rag.retriever import get_retriever

# IMPORTANT: Use host.docker.internal inside Docker
llm = OllamaLLM(
    model="tinyllama",
    base_url="http://host.docker.internal:11434"
)

retriever = get_retriever()


def process_question(question: str):
    docs = retriever.invoke(question)

    if not docs:
        return "No relevant documentation found."

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a Kubernetes troubleshooting assistant.

    STRICT RULES:
    - Answer using ONLY the provided context.
    - Do NOT explain about context.
    - Do NOT say "if context is insufficient".
    - Give direct technical answer.
    - If nothing relevant exists, say: "No relevant documentation found."

    Context:
    {context}

    Question:
    {question}

    Final Answer:
    """

    response = llm.invoke(prompt)
    return response