from dishka import make_async_container

from app.di.database import AsyncSessionProvider
from app.di.repos import ReposProvider
from app.di.services import ServicesProvider

container = make_async_container(
    AsyncSessionProvider(),
    ServicesProvider(),
    ReposProvider(),
)