import re
from typing import Optional

from pydantic import BaseModel, field_validator


class ClientDto(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    document: Optional[str] = None

    @field_validator('name')
    def only_letters_and_blank_space(cls, name: str) -> str:
        if not name or name.strip() == "":
            return name
        if not re.fullmatch(r'[A-Za-zÀ-ÿ ]+', name):
            raise ValueError("Nome inválido")
        return name

    @field_validator('name', 'email', 'document')
    def check_max_length(cls, field: str) -> str:
        if len(field) > 200:
            raise ValueError("Tamanho do campo é inválido")
        return field
