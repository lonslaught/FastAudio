from pydantic import UUID4, BaseModel


class AudioInDb(BaseModel):
    data: bytes
    filename: str
    user_id: UUID4


class AudioFromDb(BaseModel):
    data: bytes
    filename: str
