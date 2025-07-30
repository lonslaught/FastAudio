from typing import Generic, Type, TypeVar
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

ModelType = TypeVar("ModelType", bound=DeclarativeBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class BaseRepo(Generic[ModelType, CreateSchemaType]):
    def __init__(self, session: AsyncSession, model: Type[ModelType]) -> None:
        self.session = session
        self.model = model

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        obj_dict = obj_in.model_dump()
        db_obj = self.model(**obj_dict)
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def get_by_id(self, id: UUID) -> ModelType | None:
        query = select(self.model).filter(self.model.id == id)  # type: ignore
        records = await self.session.execute(query)
        db_obj = records.scalars().first()
        return db_obj
