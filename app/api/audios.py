import io
from uuid import UUID

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Request, UploadFile
from fastapi.responses import StreamingResponse

from app.services.audios import AudiosService
from app.services.users import UsersService

router = APIRouter(prefix="/audios", tags=["Audios"])

@router.post("/upload/")
@inject
async def upload_audio(request: Request, user_id: UUID, user_token: UUID, file: UploadFile, users_service: FromDishka[UsersService], audio_service: FromDishka[AudiosService]) -> str:
    await users_service.validate_user_token(user_id=user_id, user_token=user_token)

    audio_id = await audio_service.save_audiofile(user_id=user_id, file=file)

    url = request.url_for("download_audio")
    url_with_params = f"{url}?user_id={user_id}&audio_id={audio_id}"
    return url_with_params


@router.get("/download/", name="download_audio")
@inject
async def download_audio(user_id: UUID, audio_id: UUID, audio_service: FromDishka[AudiosService]) -> StreamingResponse:
    audio_dto = await audio_service.get_audio(audio_id=audio_id, user_id=user_id)

    return StreamingResponse(
        io.BytesIO(audio_dto.data),
        media_type="audio/mpeg",
        headers={
            "Content-Disposition": f'attachment; filename="{audio_dto.filename}.mp3"'
        }
    )

    
    