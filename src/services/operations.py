from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import datetime

from src.db.db import get_session
from src.models.operation import Operation
from src.models.schemas.operation.operation_request import OperationRequest


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def all(self):
        operations = self.session.query(Operation).order_by(Operation.id.desc()).all()
        return operations

    def get(self, operation_id: int) -> Operation:
        operation = (
            self.session.query(Operation).filter(Operation.id == operation_id).first()
        )
        return operation

    def add(self, operation_schema: OperationRequest, called_user_id: int) -> Operation:
        datetime_ = datetime.utcnow()
        operation = Operation(
            **operation_schema.dict(), called_at=datetime_, called_by=called_user_id
        )
        self.session.add(operation)
        self.session.commit()
        return operation
