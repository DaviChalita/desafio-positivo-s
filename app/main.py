from fastapi import FastAPI

from app.controllers.client_controller import router as client_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(client_router)

    return app


app = create_app()
