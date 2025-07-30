from typing import AsyncIterator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import Session


class AsyncSessionProvider(Provider):

    @provide(scope=Scope.REQUEST)
    async def provide_db_session(self) -> AsyncIterator[AsyncSession]:
        async with Session() as session:
            try:
                yield session
            finally:
                await session.close()
