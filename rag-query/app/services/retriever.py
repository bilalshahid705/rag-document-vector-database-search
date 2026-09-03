from langchain_core.documents import Document
from app.services.vector_store import vector_store

def similarity_search(
    query: str,
    top_k: int = 5,
) -> list[Document]:

    return vector_store.similarity_search(
        query=query,
        k=top_k,
    )