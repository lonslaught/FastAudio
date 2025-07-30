from pydantic import PostgresDsn

from app.configs.base import DeploySettings


class DatabaseSettings(DeploySettings):
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_USER: str

    ECHO: bool = False
    ECHO_POOL: bool = False
    MAX_OVERFLOW: int = 2
    POOL_SIZE: int = 7
    POOL_RECYCLE: int = 100

    naming_convention: dict[str, str] = {
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "ix": "ix_%(column_0_label)s",
        "pk": "pk_%(table_name)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    }

    @property
    def POSTGRES_DSN(self) -> PostgresDsn:
        _db = self.POSTGRES_DB
        _host = self.POSTGRES_HOST
        _password = self.POSTGRES_PASSWORD
        _port = self.POSTGRES_PORT
        _user = self.POSTGRES_USER
        url = f"postgresql+asyncpg://{_user}:{_password}@{_host}:{_port}/{_db}"
        return url


db_settings = DatabaseSettings()
