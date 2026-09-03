from fastapi import APIRouter

from app.api.v1.query import router as query_router

api_router = APIRouter()

@api_router.get("/")
async def home():
    return {"message": "Welcome to the RAG Indexing"}


@api_router.get("/health")
async def health_check():
    return {"status": "API is working fine!"}


api_router.include_router(query_router)