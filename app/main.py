from fastapi import FastAPI

from app.controllers.client_controller import router as client_router


def create_app() -> FastAPI:
    application = FastAPI()
    application.include_router(client_router)

    return application


app = create_app()
