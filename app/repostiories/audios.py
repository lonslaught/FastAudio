from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.audios import Audio
from app.repostiories.base import BaseRepo
from app.schemas.audios import AudioInDb


class AudiosRepo(BaseRepo[Audio, AudioInDb]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session, model=Audio)

    async def get_audio(self, id: UUID, user_id: UUID) -> Audio | None:
        query = select(self.model).filter(self.model.id == id).filter(self.model.user_id==user_id)
        records = await self.session.execute(query)
        db_obj = records.scalars().first()
        return db_obj