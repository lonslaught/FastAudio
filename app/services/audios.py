import io
from pathlib import Path
from uuid import UUID

from fastapi import HTTPException, UploadFile, status
from pydub import AudioSegment  # type: ignore
from pydub.exceptions import CouldntDecodeError  # type: ignore

from app.repostiories.audios import AudiosRepo
from app.schemas.audios import AudioFromDb, AudioInDb


class AudiosService:
    def __init__(self, audios_repo: AudiosRepo) -> None:
        self.audios_repo = audios_repo
        
    def validate_file_format(self, filename: str | None) -> None:
        if not filename or not filename.endswith(".wav"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File must be WAV")
    
    async def convert_wav_to_mp3_bytes(self, file: UploadFile) -> bytes:
        wav_bytes = await file.read()
        try:
            wav_audio = AudioSegment.from_file(io.BytesIO(wav_bytes), format="wav")
        except CouldntDecodeError:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to decode WAV file")

        mp3_io = io.BytesIO()
        try:
            wav_audio.export(mp3_io, format="mp3")
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to convert to MP3")

        mp3_bytes = mp3_io.getvalue()
        return mp3_bytes
    
    async def save_audiofile(self, user_id: UUID, file: UploadFile) -> UUID:
        self.validate_file_format(filename=file.filename)
        mp3_bytes = await self.convert_wav_to_mp3_bytes(file=file)

        audio_in_db = AudioInDb(
            data=mp3_bytes,
            filename=Path(file.filename or "").stem,
            user_id=user_id,
        )
        audio_from_db = await self.audios_repo.create(audio_in_db)

        return audio_from_db.id
    
    async def get_audio(self, user_id: UUID, audio_id: UUID) -> AudioFromDb:
        audio_from_db = await self.audios_repo.get_audio(id=audio_id, user_id=user_id)

        if not audio_from_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Audio not found")

        audio_dto = AudioFromDb(
            data=audio_from_db.data,
            filename=audio_from_db.filename,
        )
        return audio_dto
