from pydantic import BaseModel


class ClientDto(BaseModel):
    name: str
    email: str
    document: str