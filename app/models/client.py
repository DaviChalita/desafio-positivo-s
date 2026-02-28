from datetime import datetime
from typing import TypedDict


class Client(TypedDict):
    name: str
    email: str
    document: str
    active: bool
    created_at: datetime
    updated_at: datetime
