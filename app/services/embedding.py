from openai import OpenAI

from app.config import settings


client = OpenAI(
    api_key=settings.openai_api_key
)


def create_embeddings(chunks: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunks,
    )

    return [item.embedding for item in response.data]