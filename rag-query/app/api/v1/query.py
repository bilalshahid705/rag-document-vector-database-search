from fastapi import APIRouter

from app.schemas.query import QueryRequest
from app.services.retriever import similarity_search
from app.services.llm import llm_response

router = APIRouter(tags=["RAG"])

@router.post("/query")
def query_documents(request: QueryRequest):
    # 1. Retrieve relevant document chunks
    results = similarity_search(
        query=request.question,
        top_k = 5,
    )

    # 2. Generate answer using retrieved context
    answer = llm_response(
        question=request.question,
        documents=results,
    )

    # 3. Return answer and sources
    return {
        "question": request.question,
        "answer": answer,
        # "sources": [
        #     {
        #         "content": document.page_content,
        #         "metadata": document.metadata,
        #     }
        #     for document in results
        # ],
    }