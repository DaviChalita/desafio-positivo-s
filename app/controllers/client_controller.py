from typing import Annotated

from fastapi import Depends, APIRouter
from pymongo.asynchronous.database import AsyncDatabase

from app.database_conn.database_conn_mongodb import get_session_mongo
from app.dtos.client_dto import ClientDto
from app.services.create_client_service import CreateClientService
from app.services.delete_client_service import DeleteClientService
from app.services.get_client_service import GetClientService
from app.services.update_client_service import UpdateClientService

SessionClient = Annotated[AsyncDatabase, Depends(get_session_mongo)]

router = APIRouter(prefix="/clients")


@router.post("/")
async def create_clients(client_dto: ClientDto, session: SessionClient):
    return await CreateClientService(session).create_client(client_dto)


@router.get("/")
async def get_all_clients(session: SessionClient):
    return await GetClientService(session).get_all_clients()


@router.get("/{client_id}")
async def get_client_by_id(client_id: str, session: SessionClient):
    return await GetClientService(session).get_client_by_id(client_id)

@router.put("/{client_id}")
async def update_client_by_id(client_id: str, client_dto: ClientDto, session: SessionClient):
    return await UpdateClientService(session).update_client_by_id(client_id, client_dto)


@router.patch("/{client_id}")
async def update_client_partially_by_id(client_id: str, session: SessionClient):
    return await UpdateClientService(session).update_client_partially_by_id(client_id)


@router.delete("/{client_id}")
async def delete_client_by_id(client_id: str, session: SessionClient):
    return await DeleteClientService(session).delete_client_by_id(client_id)
