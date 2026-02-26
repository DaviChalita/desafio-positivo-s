from sqlalchemy.orm import Session

from app.repositories.client_repository import ClientRepository


class GetClientService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = ClientRepository(db)

    def get_all_clients(self):
        return self.repo.get_all_clients()
