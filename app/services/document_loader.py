from langchain_community.document_loaders import (
    PyPDFLoader,
)
from dotenv import load_dotenv

load_dotenv()


def pdf_loader(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} document(s) from PDF")
    for i, doc in enumerate(documents):
        print(f"Document {i+1} Content Preview: {doc.page_content[:100]}...")
        print(f"Metadata: {doc.metadata}")
        
    return documents


if __name__ == "__main__":
    pdf_loader("app/docs/faqs.pdf")