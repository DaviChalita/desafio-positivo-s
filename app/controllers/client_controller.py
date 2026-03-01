from typing import Annotated

from fastapi import Depends, APIRouter
from pymongo.asynchronous.database import AsyncDatabase

from app.database_conn.database_conn_mongodb import get_session_mongo
from app.dtos.client_create_dto import ClientCreateDto
from app.dtos.client_dto import ClientDto
from app.services.create_client_service import CreateClientService
from app.services.delete_client_service import DeleteClientService
from app.services.get_client_service import GetClientService
from app.services.update_client_service import UpdateClientService

SessionClient = Annotated[AsyncDatabase, Depends(get_session_mongo)]

router = APIRouter(prefix="/clients")


@router.post("", name="Criar Clientes")
async def create_clients(client_dto: ClientCreateDto, session: SessionClient):
    return await CreateClientService(session).create_client(client_dto)


@router.get("", name="Buscar Todos Clientes")
async def get_all_clients(session: SessionClient):
    return await GetClientService(session).get_all_clients()


@router.get("/{client_id}", name="Buscar Cliente Por Id")
async def get_client_by_id(client_id: str, session: SessionClient):
    return await GetClientService(session).get_client_by_id(client_id)


@router.put("/{client_id}", name="Alterar Cliente Por Id")
async def update_client_by_id(client_id: str, client_dto: ClientDto, session: SessionClient):
    return await UpdateClientService(session).update_client_by_id(client_id, client_dto)


@router.patch("/{client_id}", name="Alterar Status de Ativação do Cliente Por Id")
async def change_client_activation_status_by_id(client_id: str, session: SessionClient):
    return await UpdateClientService(session).change_client_activation_status_by_id(client_id)


@router.delete("/{client_id}", name="Deletar Cliente Por Id")
async def delete_client_by_id(client_id: str, session: SessionClient):
    return await DeleteClientService(session).delete_client_by_id(client_id)
