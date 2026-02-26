from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


def load_and_split_documents():
    loader = TextLoader("docs/k8s.txt")
    documents = loader.load()

    splitter = CharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)
    return docs