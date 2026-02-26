from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


def get_retriever():
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text",
        base_url="http://host.docker.internal:11434"
    )

    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    return vectorstore.as_retriever()