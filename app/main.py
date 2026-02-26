from fastapi import FastAPI

from app.dtos.client_dto import ClientDto
from app.services.create_client_service import CreateClientService

app = FastAPI()

