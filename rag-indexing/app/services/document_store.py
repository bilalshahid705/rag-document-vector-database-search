from app.services.vector_store import vector_store


def store_document_chunks(
    chunks,
    embeddings: list[list[float]],
    filename: str,
) -> int:
    if len(chunks) != len(embeddings):
        raise ValueError(
            "Number of chunks and embeddings must be the same."
        )

    texts = [chunk.page_content for chunk in chunks]
    metadatas = [
        {
            "source": filename,
            "page": chunk.metadata.get("page"),
            "page_label": chunk.metadata.get("page_label"),
            "chunk_index": index,
        }
        for index, chunk in enumerate(chunks)
    ]
    ids = [f"{filename}:{index}" for index in range(len(chunks))]

    vector_store.add_embeddings(
        texts=texts,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )

    return len(chunks)
