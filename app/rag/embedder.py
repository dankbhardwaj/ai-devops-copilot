from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from app.rag.loader import load_and_split_documents


def create_vector_store():
    docs = load_and_split_documents()

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    print("Vector store created successfully!")