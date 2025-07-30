from fastapi import FastAPI

def get_app() -> FastAPI:
    app = FastAPI(
        debug=True # STAGE != "prod",  # Заменить
    )

    return app

app = get_app()
