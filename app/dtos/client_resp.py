from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ClientDtoResp(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: Optional[str] = None
    email: Optional[str] = None
    document: Optional[str] = None
    active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {
        "populate_by_name": True,
    }
