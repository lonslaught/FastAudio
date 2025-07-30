from datetime import UTC, datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, String
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.dialects.postgresql import UUID as sqlUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database.session import Base


class Audio(Base):
    __tablename__ = "audios"

    id: Mapped[UUID] = mapped_column(sqlUUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=lambda: datetime.now(UTC).replace(tzinfo=None))
    data: Mapped[bytes] = mapped_column(BYTEA, nullable=False)
    filename: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[UUID] = mapped_column(sqlUUID(as_uuid=True), nullable=False)
