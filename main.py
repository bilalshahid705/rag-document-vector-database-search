from fastapi import FastAPI

from app.api.document import router as document_router


app = FastAPI(
    title="RAG Admin API",
)


app.include_router(document_router)