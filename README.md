# FastAudio

FastAudio — сервис для быстрой загрузки WAV-аудиофайлов и конвертации их в формат MP3 с привязкой к каждому пользователю.

## Установка и запуск (локально)

1. Склонируйте репозиторий:

```sh
git clone https://github.com/lonslaught/FastAudio.git
```

2. Перейдите в директорию с проектом:

```sh
cd FastAudio
```

3. Создайте `.env`-файл в директории `FastAudio/deploy/local` на основе шаблона `.env.template`, расположенного в корне проекта:

```env
# APP
API_PORT=8000
API_HOST=0.0.0.0  # Не изменяйте это значение

# DATABASE
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=fastaudio_db
POSTGRES_HOST=fastaudio_database_local  # Не изменяйте это значение
POSTGRES_PORT=5432  # Порт подключения к БД
```

4. Запустите проект:

```sh
make local
```

5. Для просмотра доступных команд:

```sh
make help
```

6. После запуска проекта документация API будет доступна по адресу:

```
http://127.0.0.1:{API_PORT}/api/fastaudio/docs
```

_Замените `{API_PORT}` на порт, указанный в `.env` (например, `8000`)._
