from enum import StrEnum
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from starlette.config import Config


class AppStageEnum(StrEnum):
    LOCAL = "LOCAL"
    PROD = "PROD"

config_stage = Config("deploy/.stage.env")
STAGE = config_stage("STAGE", cast=AppStageEnum)


def get_env_file_path(stage: AppStageEnum) -> Path:
    if stage == AppStageEnum.LOCAL:
        return Path("deploy/local/.env")
    elif stage == AppStageEnum.PROD:
        return Path("deploy/prod/.env")
    raise ValueError(f"Invalid stage: {stage}")


class DeploySettings(BaseSettings):
    env_file = get_env_file_path(STAGE)

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=(".env.template", env_file),
        extra="ignore",
    )
