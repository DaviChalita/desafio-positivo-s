import logging

from fastapi import HTTPException
from pymongo.asynchronous.database import AsyncDatabase

from app.repositories.client_repository import ClientRepository
from app.services.get_client_service import GetClientService

logger = logging.getLogger(__name__)


class DeleteClientService:
    def __init__(self, db: AsyncDatabase):
        self.repo = ClientRepository(db)
        self.get_client_service = GetClientService(db)

    async def delete_client_by_id(self, client_id: str):
        await self.get_client_service.get_client_by_id(client_id)

        try:
            await self.repo.delete_client_by_id(client_id)
            return {"msg": "Usuário excluído com sucesso"}
        except Exception:
            logger.exception("Erro ao excluir cliente")
            raise HTTPException(status_code=500, detail="Erro ao tentar excluir cliente")
