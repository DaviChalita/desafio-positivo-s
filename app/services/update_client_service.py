import logging

from fastapi import HTTPException
from pymongo.asynchronous.database import AsyncDatabase

from app.dtos.client_dto import ClientDto
from app.repositories.client_repository import ClientRepository
from app.services.get_client_service import GetClientService

logger = logging.getLogger(__name__)


class UpdateClientService:
    def __init__(self, db: AsyncDatabase):
        self.repo = ClientRepository(db)
        self.get_client_service = GetClientService(db)

    async def update_client_by_id(self, client_id: str, client_dto: ClientDto):
        client = await self.get_client_service.get_client_by_id(client_id)

        try:
            await self.repo.update_client_by_id(client_id, client_dto, client)
            return {"msg": "Usuário alterado com sucesso"}
        except Exception:
            logger.exception("Erro ao alterar cliente")
            raise HTTPException(status_code=500, detail="Erro ao tentar alterar o cliente")

    async def change_client_activation_status_by_id(self, client_id: str):
        await self.get_client_service.get_client_by_id(client_id)

        try:
            await self.repo.change_client_activation_status_by_id(client_id)
            return {"msg": "Status de ativação do cliente alterado com sucesso"}
        except Exception:
            logger.exception("Erro ao alterar status de ativação do cliente")
            raise HTTPException(status_code=500, detail="Erro ao tentar alterar o status de ativação do cliente")
