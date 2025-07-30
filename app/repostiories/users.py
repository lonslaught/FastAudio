from sqlalchemy.ext.asyncio import AsyncSession

from app.models.users import User
from app.repostiories.base import BaseRepo
from app.schemas.users import UserInDb


class UsersRepo(BaseRepo[User, UserInDb]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session, model=User)
