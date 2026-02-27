from typing import Annotated

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.database_conn.database_conn import get_session
from app.dtos.client_dto import ClientDto
from app.services.create_client_service import CreateClientService
from app.services.get_client_service import GetClientService
from app.services.update_client_service import UpdateClientService

SessionClient = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/clients")


@router.post("/")
async def create_clients(client_dto: ClientDto, session: SessionClient):
    return CreateClientService(session).create_client(client_dto)


@router.get("/")
async def get_all_clients(session: SessionClient):
    return GetClientService(session).get_all_clients()

@router.get("/{client_id}")
async def get_client_by_id(client_id: int, session: SessionClient):
    return GetClientService(session).get_client_by_id(client_id)

@router.put("/{client_id}")
async def update_client_by_id(client_id: int, client_dto: ClientDto, session: SessionClient):
    return UpdateClientService(session).update_client_by_id(client_id, client_dto)