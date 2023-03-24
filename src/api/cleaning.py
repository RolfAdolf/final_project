from fastapi import APIRouter
import threading

from src.services.utils.models_clearing import CleaningService
from src.api.ml import trained_models
from src.core.settings import settings


router = APIRouter(prefix="/cleaning", tags=["cleaning"])


cleaning_service = CleaningService()


@router.on_event("startup")
def start():
    task = threading.Thread(
        target=cleaning_service.models_cleaning,
        args=[trained_models, settings.model_expire_seconds],
    )
    task.start()


@router.on_event("shutdown")
def stop():
    cleaning_service.delete_all()
