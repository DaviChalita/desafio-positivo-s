import re
from typing import Optional

from pydantic import BaseModel, field_validator


def check_max_length(field: str, size: int):
    if len(field) > size:
        raise ValueError("Tamanho do campo é inválido")


class ClientDto(BaseModel):
    name: Optional[str] = None
    # email pode ser validado através de um email de confirmação de cadastro, o regex de email é inválido em muitos casos
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
        # validacao sem máscara
        if len(document) != 9:
            raise ValueError("Tamanho do campo é inválido")
        if not re.fullmatch(r"^\d{8}[0-9X]$", document):
            raise ValueError("Documento inválido")
        return document
