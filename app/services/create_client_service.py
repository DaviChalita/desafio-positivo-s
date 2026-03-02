import logging

from fastapi import HTTPException
from pymongo.asynchronous.database import AsyncDatabase

from app.dtos.client_dto import ClientDto
from app.repositories.client_repository import ClientRepository

logger = logging.getLogger(__name__)


class CreateClientService:

    def __init__(self, db: AsyncDatabase):
        self.repo = ClientRepository(db)

    async def create_client(self, client_dto: ClientDto) -> dict:
        try:
            await self.repo.create_client_repository(client_dto)
            return {"message": "Usuário inserido com sucesso"}
        except Exception:
            logger.exception("Erro ao salvar cliente")
            raise HTTPException(status_code=500, detail="Erro ao tentar salvar o cliente")
