from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.document import router as document_router

app = FastAPI(
    title="RAG Admin API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:8000", "https://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)




app.include_router(document_router)