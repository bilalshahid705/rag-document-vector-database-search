from langchain_postgres import PGVector

from app.core.config import settings
from app.services.embedding import embeddings

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="documents",
    connection=settings.DATABASE_URL,
    embedding_length=1536,
    use_jsonb=True,
)