from datetime import datetime

from bson import ObjectId
from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.database import AsyncDatabase

from app.dtos.client_dto import ClientDto
from app.models.client import Client
from app.dtos.client_resp import ClientDtoResp


class ClientRepository:
    def __init__(self, session: AsyncDatabase):
        self.session: AsyncCollection = session['clients']

    async def create_client_repository(self, client_dto: ClientDto) -> None:
        await self.session.insert_one(
            Client(name=client_dto.name, email=client_dto.email, document=client_dto.document, active=True,
                   created_at=datetime.now()))

    async def get_all_clients(self):
        clients: list[ClientDtoResp] = []
        async for doc in self.session.find({}):
            clients.append(ClientDtoResp.model_validate({**doc, '_id': str(doc['_id'])}).model_dump(by_alias=False))

        return clients

    async def get_client_by_id(self, client_id: str) -> ClientDtoResp:
        client = await self.session.find_one({'_id': ObjectId(client_id)})
        return ClientDtoResp.model_validate({**client, '_id': str(client['_id'])}).model_dump(by_alias=False)

    async def update_client_by_id(self, client_id: str, client_dto: ClientDto, client: ClientDtoResp):
        await self.session.replace_one({'_id': ObjectId(client_id)},
                                       {**client_dto.model_dump(exclude_unset=True),
                                        'active': client['active'],
                                        'created_at': client['created_at'],
                                        'updated_at': datetime.now(), })

    async def change_client_activation_status_by_id(self, client_id: str):
        await self.session.update_one({'_id': ObjectId(client_id)},
                                      [{'$set': {
                                          'active': {'$not': ['$active']},
                                          'updated_at': datetime.now()}}])

    async def delete_client_by_id(self, client_id: str):
        await self.session.delete_one({"_id": ObjectId(client_id)})
