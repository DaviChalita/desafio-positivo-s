from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.dtos.client_dto import ClientDto
from app.models.client import Client


class ClientRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_client_repository(self, client_dto: ClientDto) -> None:
        self.session.add(Client(name=client_dto.name, email=client_dto.email, document=client_dto.document,
                                created_at=datetime.now()))
        self.session.commit()

    def get_all_clients(self):
        return self.session.scalars(select(Client)).all()
