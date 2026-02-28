from app.dtos.client_dto import ClientDto


class ClientCreateDto(ClientDto):
    name: str
    email: str
    document:str