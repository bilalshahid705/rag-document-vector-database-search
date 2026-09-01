from pathlib import Path

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.document_loader import pdf_loader
from app.services.chunker import chunk_document
from app.services.embedding import create_embeddings


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    # Check file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    # Read file
    content = await file.read()

    # Check file size
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File size must not exceed 2 MB.",
        )

    # Create upload directory
    
    upload_dir = Path("documents")
    upload_dir.mkdir(exist_ok=True)

    # Save file
    file_path = upload_dir / file.filename

    with open(file_path, "wb") as f:
        f.write(content)

    # 1. Extract PDF pages
    documents = pdf_loader(str(file_path))

    # 2. Create chunks
    chunks = chunk_document(documents)

    # 3. Create embeddings
    embeddings = create_embeddings(chunks)

    return {
        "filename": file.filename,
        "pages_loaded": len(documents),
        "chunks_created": len(chunks),
        "message": "Document processed successfully.",
    }