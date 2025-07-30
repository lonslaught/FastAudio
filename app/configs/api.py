from app.configs.base import DeploySettings


class ApiConfig(DeploySettings):
    DOCS_URL: str = "/api/fastaudio/docs/_s"
    OPENAPI_URL: str = "/api/fastaudio/docs/openapi.json"
    REDOC_URL: str = "/api/fastaudio/docs/_r"
    TITLE: str = "FastAudio API Service"



api_config = ApiConfig()
