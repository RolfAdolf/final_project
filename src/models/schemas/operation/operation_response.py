from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class OperationRequest(BaseModel):
    id: int
    method: str
    called_at: datetime
    called_by: Optional[int]
