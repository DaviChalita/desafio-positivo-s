from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.client_repository import ClientRepository


class GetClientService:
    def __init__(self, db: Session):
        self.repo = ClientRepository(db)

    def get_all_clients(self):
        return self.repo.get_all_clients()

    def get_client_by_id(self, client_id: int):
        client = self.repo.get_client_by_id(client_id)
        if client is None:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return client
