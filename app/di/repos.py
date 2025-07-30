
from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.repostiories.audios import AudiosRepo
from app.repostiories.users import UsersRepo


class ReposProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def provide_users_repo(self, session: AsyncSession) -> UsersRepo:
        repo = UsersRepo(session=session)
        return repo

    @provide
    async def provide_audio_repo(self, session: AsyncSession) -> AudiosRepo:
        repo = AudiosRepo(session=session)
        return repo