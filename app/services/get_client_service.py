from fastapi import HTTPException
from pymongo.asynchronous.database import AsyncDatabase

from app.repositories.client_repository import ClientRepository


class GetClientService:
    def __init__(self, db: AsyncDatabase):
        self.repo = ClientRepository(db)

    async def get_all_clients(self):
        return await self.repo.get_all_clients()

    async def get_client_by_id(self, client_id: str):
        client = await self.repo.get_client_by_id(client_id)
        if client is None:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return client
