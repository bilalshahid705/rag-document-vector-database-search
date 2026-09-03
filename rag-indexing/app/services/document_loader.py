from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def pdf_loader(pdf_path: str) -> list[Document]:
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError("PDF file not found")

    loader = PyPDFLoader(str(path))

    return loader.load()