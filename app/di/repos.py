
from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.repostiories.users import UsersRepo


class ReposProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def provide_users_repo(self, session: AsyncSession) -> UsersRepo:
        repo = UsersRepo(session=session)
        return repo
