from dishka import Provider, Scope, provide

from app.repostiories.audios import AudiosRepo
from app.repostiories.users import UsersRepo
from app.services.audios import AudiosService
from app.services.users import UsersService


class ServicesProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def provide_users_service(self, users_repo: UsersRepo) -> UsersService:
        service = UsersService(users_repo=users_repo)
        return service

    @provide
    async def provide_audios_service(self, audios_repo: AudiosRepo) -> AudiosService:
        service = AudiosService(audios_repo=audios_repo)
        return service