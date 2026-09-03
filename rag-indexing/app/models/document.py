from datetime import datetime, timezone

from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, SQLModel


class Document(SQLModel, table=True):
    __tablename__ = "documents"

    id: int | None = Field(
        default=None,
        primary_key=True,
    )

    document_name: str

    chunk_index: int

    content: str

    embedding: list[float] = Field(
        sa_type=Vector(1536)
    )

    doc_metadata: dict = Field(
        default_factory=dict,
        sa_type=JSONB,
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )