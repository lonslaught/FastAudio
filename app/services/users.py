from app.repostiories.users import UsersRepo
from app.schemas.users import UserInDb, UserInput, UserOutput


class UsersService:
    def __init__(self, users_repo: UsersRepo) -> None:
        self.users_repo = users_repo

    async def create_user(self, user_input: UserInput) -> UserOutput:
        user_in_db = UserInDb(
            username=user_input.username
        )
        user_from_db = await self.users_repo.create(obj_in=user_in_db)

        user_output = UserOutput(
            id=user_from_db.id,
            token=user_from_db.token,
            username=user_from_db.username,
        )
        return user_output