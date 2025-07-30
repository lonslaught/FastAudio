from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.schemas.users import UserInput, UserOutput
from app.services.users import UsersService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserOutput)
@inject
async def create_user(user_input: UserInput, users_service: FromDishka[UsersService]) -> UserOutput:
    """
    Эндпоинт для создания пользователя
    """
    user_output = await users_service.create_user(user_input=user_input)
    return user_output
