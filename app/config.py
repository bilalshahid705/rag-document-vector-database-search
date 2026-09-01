from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str
    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()

# from importlib import metadata
# import os
# from dotenv import load_dotenv
# from langchain_postgres import PGVector
# from langchain_openai import OpenAIEmbeddings
# from langchain_core.documents import Document

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# def connect_to_database():
#     # Connect to Supabase pgvector

#     embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

#     print(f"DATABASE_URL: {DATABASE_URL}")

#     vectorstore = PGVector(
#         embeddings=embeddings,
#         collection_name="production_document",
#         connection=DATABASE_URL,
#         use_jsonb=True,
#     )

#     return vectorstore

# def verify_connection(vectorstore):
#     # Verify the connection works

#     test_docs = Document(
#         page_content="This is a test document to verify Supabase",
#         metadata={"test": True}
#     )

#     try:
#         ids = vectorstore.add_documents([test_docs])
#         print(f"Added test document: {ids[0]}")

#         results = vectorstore.similarity_search("test document")
#         if results:
#             print(f"Search Works: {results[0].page_content}")

        
#         vectorstore.delete(ids)
        
#         return True

#     except Exception as e:
#         print(f"Error: {e}")
#         return False


