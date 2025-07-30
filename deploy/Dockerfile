FROM python:3.12
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates ffmpeg
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

# Установка рабочей директории внутри контейнера
WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache

COPY . /app/