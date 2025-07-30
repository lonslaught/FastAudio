from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.api.users import router as users_router
from app.configs.api import api_config
from app.configs.base import STAGE, AppStageEnum
from app.di import container


def get_app() -> FastAPI:
    app = FastAPI(
        debug=STAGE != AppStageEnum.PROD,
        docs_url=api_config.DOCS_URL,
        openapi_url=api_config.OPENAPI_URL,
        redoc_url=api_config.REDOC_URL,
        title=api_config.TITLE,
    )
    setup_dishka(app=app, container=container)

    app.include_router(users_router)

    return app

app = get_app()
