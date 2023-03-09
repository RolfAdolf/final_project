from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ModelResponse(BaseModel):
    id: int
    type: str
    created_at: datetime
    created_by: Optional[int]
