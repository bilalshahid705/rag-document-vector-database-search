from sqlmodel import Session

from app.core.database import engine
from app.models.document import Document


def store_document_chunks(
    chunks,
    embeddings: list[list[float]],
    filename: str,
) -> int:

    if len(chunks) != len(embeddings):
        raise ValueError(
            "Number of chunks and embeddings must be the same."
        )

    documents = []

    for index, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):
        document = Document(
            document_name=filename,
            chunk_index=index,
            content=chunk.page_content,
            embedding=embedding,
            doc_metadata={
                "source": filename,
                "page": chunk.metadata.get("page"),
                "page_label": chunk.metadata.get("page_label"),
            },
        )

        documents.append(document)

    with Session(engine) as session:
        session.add_all(documents)
        session.commit()

    return len(documents)