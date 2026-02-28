import re
from typing import Optional

from pydantic import BaseModel, field_validator


def check_max_length(field: str, size: int):
    if len(field) > size:
        raise ValueError("Tamanho do campo é inválido")


class ClientDto(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    document: Optional[str] = None

    @field_validator('name')
    def validate_name(cls, name: str) -> str:
        if not name or name.strip() == "":
            return name
        check_max_length(name, 200)
        if not re.fullmatch(r'[A-Za-zÀ-ÿ ]+', name):
            raise ValueError("Nome inválido")
        return name

    @field_validator('email')
    def validate_email(cls, email: str) -> str:
        check_max_length(email, 200)
        return email

    @field_validator('document')
    def validate_document(cls, document: str) -> str:
        if not document or document.strip() == "":
            return document
        check_max_length(document, 200)
        #validacao para rg, outros podem ser adicionados tambem
        if not re.fullmatch(r"^(\d{2}\.?\d{3}\.?\d{3}-?[\dXx]|\d{9,10})$", document):
            raise ValueError("Documento inválido")
        return document
