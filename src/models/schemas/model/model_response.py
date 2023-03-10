from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ModelResponse(BaseModel):
    id: int
    model_type: str
    created_by: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True
