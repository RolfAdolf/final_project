import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse

from src.models.schemas.operation.operation_request import OperationRequest
from src.models.schemas.operation.operation_response import OperationResponse
from src.services.operations import OperationsService
from src.services.users import get_current_user_id


router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/all', response_model=List[OperationResponse], name="Получить все")
def get(
        operation_service: OperationsService = Depends(),
        called_user_id: int = Depends(get_current_user_id),
        ):
    """
    Получить все операции.
    """
    operations = operation_service.all()
    return operations


@router.get('/get/{operation_id}', response_model=OperationResponse, name="Получить одну")
def get(
        operation_id: int,
        operations_service: OperationsService = Depends(),
        called_user_id: int = Depends(get_current_user_id)
        ):
    """
    Получить одну операцию по id.
    """
    return get_with_check(operation_id, operations_service)


def get_with_check(operation_id: int, operations_service: OperationsService):
    result = operations_service.get(operation_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Операция не найдена")
    return result
