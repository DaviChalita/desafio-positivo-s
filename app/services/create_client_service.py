import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.dtos.client_dto import ClientDto
from app.repositories.client_repository import ClientRepository

logger = logging.getLogger(__name__)


class CreateClientService:

    def __init__(self, db: Session):
        self.db = db
        self.repo = ClientRepository(db)

    def create_client(self, client_dto: ClientDto) -> dict:
        try:
            self.repo.create_client_repository(client_dto)
            return {"message": "Usuário inserido com sucesso"}
        except Exception:
            logger.exception("Erro ao salvar cliente")
            raise HTTPException(status_code=500, detail="Erro ao tentar salvar o cliente")
