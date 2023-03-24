from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from src.models.schemas.operation.operation_request import OperationType


class OperationResponse(BaseModel):
    id: int
    operation: OperationType
    called_at: datetime
    called_by: Optional[int]

    class Config:
        orm_mode = True
