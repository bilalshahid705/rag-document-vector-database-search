from fastapi import APIRouter

from app.api.v1.document import router as document_router

api_router = APIRouter()

@api_router.get("/")
async def home():
    return {"message": "Welcome to the RAG Indexing"}


@api_router.get("/health")
async def health_check():
    return {"status": "API is working fine!"}


api_router.include_router(document_router)