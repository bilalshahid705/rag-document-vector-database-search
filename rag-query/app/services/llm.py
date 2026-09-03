from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.core.config import settings


LLM_MODEL = "gpt-4o-mini"


llm = ChatOpenAI(
    model=LLM_MODEL,
    api_key=settings.OPENAI_API_KEY,
    temperature=0,
)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a helpful RAG question-answering assistant.

Answer the user's question using ONLY the information
provided in the context.

Rules:
- Do not use information outside the provided context.
- Do not make up or hallucinate information.
- If the answer cannot be found in the context, say:
  "I don't have enough information to answer that."
- Give a clear and concise answer.
- Do not mention the context or retrieval process.

Context:
{context}
""",
        ),
        (
            "human",
            "{question}",
        ),
    ]
)


def llm_response(
    question: str,
    documents: list[Document],
) -> str:

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    messages = prompt.format_messages(
        question=question,
        context=context,
    )

    response = llm.invoke(messages)

    return response.content