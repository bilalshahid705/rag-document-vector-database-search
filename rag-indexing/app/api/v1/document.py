from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_loader import pdf_loader
from app.services.chunker import chunk_document
from app.services.vector_store import vector_store

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    if not file.filename or not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    # Save file
    file_path = f"/tmp/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # PDF → Documents
    documents = pdf_loader(file_path)

    # Documents → Chunks
    chunks = chunk_document(documents)

    # Add useful metadata
    for index, chunk in enumerate(chunks):
        chunk.metadata["document_name"] = file.filename
        chunk.metadata["chunk_index"] = index

    # Chunks → Embeddings → PGVector
    vector_store.add_documents(chunks)

    return {
        "message": "Document indexed successfully.",
        "document_name": file.filename,
        "chunks": len(chunks),
    }