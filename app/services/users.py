from uuid import UUID

from fastapi import HTTPException, status

from app.models.users import User
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
    
    async def get_user_by_id(self, user_id: UUID) -> User:
        user = await self.users_repo.get_by_id(id=user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        return user
    
    async def validate_user_token(self, user_id: UUID, user_token: UUID) -> None:
        user = await self.get_user_by_id(user_id=user_id)
        if user.token != user_token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

