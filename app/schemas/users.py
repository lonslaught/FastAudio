from pydantic import UUID4, BaseModel, Field


class UserInput(BaseModel):
    username: str = Field(..., description="Имя пользователя")


class UserOutput(BaseModel):
    id: UUID4 = Field(..., description="Идентификатор пользователя")
    token: UUID4 = Field(..., description="Уникальный токен доступа пользователя")
    username: str = Field(..., description="Имя пользователя")


class UserInDb(BaseModel):
    username: str
