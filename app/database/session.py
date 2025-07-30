import json
from datetime import date, datetime

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import AsyncAdaptedQueuePool

from app.configs.db import db_settings

Base = declarative_base()


def json_dumps_default(val):
    if isinstance(val, datetime):
        return val.isoformat()
    elif isinstance(val, date):
        return val.isoformat()
    raise TypeError()


def json_serializer(d):
    return json.dumps(d, default=json_dumps_default)


engine: AsyncEngine = create_async_engine(
    echo=db_settings.ECHO,
    json_serializer=json_serializer,
    max_overflow=db_settings.MAX_OVERFLOW,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=db_settings.POOL_SIZE,
    pool_recycle=db_settings.POOL_RECYCLE,
    url=str(db_settings.POSTGRES_DSN),
)

Session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine, expire_on_commit=False, autocommit=False, autoflush=False
)
