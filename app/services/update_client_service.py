import logging

from fastapi import HTTPException
from pymongo.asynchronous.database import AsyncDatabase

from app.dtos.client_dto import ClientDto
from app.repositories.client_repository import ClientRepository

logger = logging.getLogger(__name__)


class UpdateClientService:
    def __init__(self, db: AsyncDatabase):
        self.repo = ClientRepository(db)

    async def update_client_by_id(self, client_id: str, client_dto: ClientDto):
        client = await self.repo.get_client_by_id(client_id)
        if client is None:
            raise HTTPException(status_code=404, detail="Erro ao tentar alterar o cliente")

        try:
            await self.repo.update_client_by_id(client_id, client_dto, client)
            return {"msg": "Usuário alterado com sucesso"}
        except Exception:
            logger.exception("Erro ao alterar cliente")
            raise HTTPException(status_code=500, detail="Erro ao tentar alterar o cliente")

    async def update_client_partially_by_id(self, client_id: str):
        try:
            await self.repo.change_client_activation_status_by_id(client_id)
            return {"msg": "Status de ativação do cliente alterado com sucesso"}
        except Exception:
            logger.exception("Erro ao alterar status de ativação do cliente")
            raise HTTPException(status_code=500, detail="Erro ao tentar alterar o status de ativação do cliente")
