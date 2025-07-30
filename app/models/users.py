from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.database.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    token = Column(UUID(as_uuid=True), unique=True, index=True, nullable=False, default=uuid4)
    username = Column(String(128), nullable=False)
