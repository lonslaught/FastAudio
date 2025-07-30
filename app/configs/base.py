from enum import StrEnum
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from starlette.config import Config


class AppStageEnum(StrEnum):
    LOCAL = "LOCAL"
    PROD = "PROD"

config_stage = Config("deploy/.stage.env")
STAGE = config_stage("STAGE", cast=AppStageEnum)


class DeploySettings(BaseSettings):
    if STAGE == AppStageEnum.LOCAL:
        env_file: Path = "deploy/local/.env"
    elif STAGE == AppStageEnum.PROD:
        env_file: Path = "deploy/prod/.env"

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=(".env.template", env_file),
        extra="ignore",
    )
