import chromadb
from chromadb.config import Settings

# Initialize ChromaDB
client = chromadb.Client(Settings(persist_directory="./chroma_db"))

collection = client.get_or_create_collection(name="startup_research")

def store_document(doc_id: str, content: str):
    """
    Stores document in vector database.
    """
    collection.add(
        documents=[content],
        ids=[doc_id]
    )

def query_documents(query: str, n_results: int = 3):
    """
    Searches stored documents.
    """
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results