from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    UploadFile,
)
from fastapi.responses import StreamingResponse

from typing import List

from src.models.schemas.model.model_request import ModelRequest
from src.models.schemas.model.model_response import ModelResponse
from src.services.ml.ml import MLService, TrainedModel
from src.services.users import get_current_user_role, get_current_user_id
from src.services.files import FilesService
from src.services.operations import OperationsService
from src.models.schemas.operation.operation_request import OperationRequest


router = APIRouter(prefix="/ml", tags=["ml"])

trained_models = {}


@router.get("/all", response_model=List[ModelResponse], name="Получить все")
def get_all(
    ml_service: MLService = Depends(), user_role: str = Depends(get_current_user_role)
):
    """
    Получить все модели.
    """
    if not user_role == "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Недостаточно прав."
        )
    return ml_service.all()


@router.get("/all_mine", response_model=List[ModelResponse], name="Получить все модели пользователя")
def get_mine(
    ml_service: MLService = Depends(), user_id: str = Depends(get_current_user_id)
):
    """
    Получить все модели текущего пользователя.
    """
    return ml_service.all_user_models(user_id)


@router.post("/preprocess", name="Предобработка")
def preprocess(
    file: UploadFile,
    user_id: str = Depends(get_current_user_id),
    files_service: FilesService = Depends(),
    ml_service: MLService = Depends(),
    operation_service: OperationsService = Depends(),
):
    """
    Предобработка загруженных данных.
    """
    data = files_service.upload(file.file)
    preprocessed_data = ml_service.preprocess(data)
    download_file = files_service.download(preprocessed_data)
    operation_schema = OperationRequest(**{"operation": "preprocess"})
    operation_service.add(operation_schema, user_id)
    return StreamingResponse(
        download_file,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=preprocessed_data.csv"},
    )


@router.get("/download_data", name="Скачать данные")
def get_data(
    user_id: str = Depends(get_current_user_id),
    ml_service: MLService = Depends(),
    files_service: FilesService = Depends(),
    operation_service: OperationsService = Depends(),
):
    """
    Скачать датасет в формате ".csv".
    """
    data = ml_service.return_data()
    download_file = files_service.download(data)

    operation_schema = OperationRequest(**{"operation": "download"})
    operation_service.add(operation_schema, user_id)

    return StreamingResponse(
        download_file,
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=predictive_maintenance.csv"
        },
    )


@router.post("/train_model", response_model=ModelResponse, name="Обучение модели")
def train_model(
    file: UploadFile,
    model_schema: ModelRequest = Depends(),
    user_id: str = Depends(get_current_user_id),
    files_service: FilesService = Depends(),
    ml_service: MLService = Depends(),
    operation_service: OperationsService = Depends(),
):
    """
    Обучить модель на загруженных предобработанных данных.
    """
    train_data = files_service.upload(file.file)
    train_data = ml_service.preprocess(train_data)
    trained_model = ml_service.train(train_data, model_schema.model_type)
    model = ml_service.add(model_schema, user_id)
    trained_models[model.id] = trained_model

    operation_schema = OperationRequest(**{"operation": "train"})
    operation_service.add(operation_schema, user_id)

    return model


@router.post("/predict", name="Получить предсказания")
def predict(
    file: UploadFile,
    user_id: str = Depends(get_current_user_id),
    files_service: FilesService = Depends(),
    ml_service: MLService = Depends(),
    operation_service: OperationsService = Depends(),
):

    model = ml_service.get_users_last_model(user_id)

    model = trained_models[model.id]

    test_data = files_service.upload(file.file)
    test_data = ml_service.preprocess(test_data)

    pred = ml_service.predict(test_data, model)

    download_file = files_service.download(pred)

    operation_schema = OperationRequest(**{"operation": "predict"})
    operation_service.add(operation_schema, user_id)

    return StreamingResponse(
        download_file,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=predictions.csv"},
    )
