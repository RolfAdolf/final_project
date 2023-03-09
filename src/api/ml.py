from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordRequestForm

from src.models.schemas.model.model_request import ModelRequest
from src.models.schemas.model.model_response import ModelResponse
from src.services.ml.ml import MLService, TrainedModel
from src.services.users import get_current_user_role, get_current_user_id
from src.services.files import FilesService

router = APIRouter(
    prefix='/ml',
    tags=['ml']
)


@router.get('/all', response_model=List[ModelResponse], name="Получить всех")
def get(ml_service: MLService = Depends(), user_role: str = Depends(get_current_user_role)):
    """
    Получить все модели.
    """
    if not user_role == 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Недостаточно прав.')
    return ml_service.all()


@router.get('/all_mine', response_model=List[ModelResponse], name="Получить все свои")
def get(ml_service: MLService = Depends(), user_id: str = Depends(get_current_user_id)):
    """
    Получить все свои модели.
    """
    return ml_service.all_mine(user_id)


@router.post('/preprocess', name="Предобработка")
def get(
        file: UploadFile,
        files_service: FilesService = Depends(),
        ml_service: MLService = Depends()
        ):
    """
    Предобработка данных.
    """
    data = files_service.upload(file.file)
    preprocessed_data = ml_service.preprocess(data)
    download_file = files_service.download(preprocessed_data)
    return StreamingResponse(download_file, media_type='text/csv',
                             headers={'Content-Disposition': 'attachment; filename=preprocessed_data.csv'})


