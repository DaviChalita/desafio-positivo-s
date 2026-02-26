from typing import Annotated

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.database_conn.database_conn import get_session
from app.dtos.client_dto import ClientDto
from app.services.create_client_service import CreateClientService

SessionClient = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/clients")


@router.post("/")
async def create_clients(client_dto: ClientDto, session: SessionClient):
    return CreateClientService(session).create_client(client_dto)
