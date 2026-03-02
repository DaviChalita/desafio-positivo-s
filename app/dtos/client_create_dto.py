from app.dtos.client_dto import ClientDto


class ClientCreateUpdateDto(ClientDto):
    name: str
    email: str
    document:str