from langchain_postgres import PGVector
from app.core.config import settings
from app.services.embedding import embeddings

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="documents",
    connection=settings.DATABASE_URL,
)

def similarity_search(
    query: str,
    top_k: int = 5,
):
    results = vector_store.similarity_search(
        query=query,
        k=top_k,
    )
    return results