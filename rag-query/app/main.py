from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import api_router

app = FastAPI(
    title="RAG Admin API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:8001", "https://127.0.0.1:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



app.include_router(api_router, prefix="/api/v1")
