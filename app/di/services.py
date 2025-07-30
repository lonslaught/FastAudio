from dishka import Provider, Scope, provide

from app.repostiories.users import UsersRepo
from app.services.users import UsersService


class ServicesProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def provide_auth_service(self, users_repo: UsersRepo) -> UsersService:
        service = UsersService(users_repo=users_repo)
        return service
