import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.client_repository import ClientRepository

logger = logging.getLogger(__name__)


class DeleteClientService:
    def __init__(self, db: Session):
        self.repo = ClientRepository(db)

    def delete_client_by_id(self, client_id: int):
        if self.repo.get_client_by_id(client_id) is None:
            raise HTTPException(status_code=404, detail="Erro ao tentar excluir o cliente")

        try:
            self.repo.delete_client_by_id(client_id)
            return {"msg": "Usuário excluído com sucesso"}
        except Exception:
            logger.exception("Erro ao excluir cliente")
            raise HTTPException(status_code=500, detail="Erro ao tentar excluir cliente")
