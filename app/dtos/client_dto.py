from typing import Optional

from pydantic import BaseModel


class ClientDto(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    document: Optional[str] = None