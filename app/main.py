from fastapi import FastAPI

from app.configs.api import api_config
from app.configs.base import STAGE, AppStageEnum


def get_app() -> FastAPI:
    app = FastAPI(
        debug=STAGE != AppStageEnum.PROD,
        docs_url=api_config.DOCS_URL,
        openapi_url=api_config.OPENAPI_URL,
        redoc_url=api_config.REDOC_URL,
        title=api_config.TITLE,
    )

    return app

app = get_app()
