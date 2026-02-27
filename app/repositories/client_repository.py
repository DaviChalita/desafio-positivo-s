from datetime import datetime

from sqlalchemy import select, Sequence, update, not_
from sqlalchemy.orm import Session

from app.dtos.client_dto import ClientDto
from app.models.client import Client


class ClientRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_client_repository(self, client_dto: ClientDto) -> None:
        self.session.add(Client(name=client_dto.name, email=client_dto.email, document=client_dto.document, active=True,
                                created_at=datetime.now()))
        self.session.commit()

    def get_all_clients(self) -> Sequence[Client]:
        return self.session.scalars(select(Client)).all()

    def get_client_by_id(self, client_id: int) -> Client:
        return self.session.scalars(select(Client).where(Client.id == client_id)).first()

    def update_client_by_id(self, client_id: int, client_dto: ClientDto):
        self.session.execute(
            update(Client).where(Client.id == client_id).values(name=client_dto.name, email=client_dto.email,
                                                                document=client_dto.document,
                                                                updated_at=datetime.now()))
        self.session.commit()

    def change_client_activation_status_by_id(self, client_id: int):
        self.session.execute(
            update(Client).where(Client.id == client_id).values(active= not_(Client.active), updated_at=datetime.now())
        )
        self.session.commit()
