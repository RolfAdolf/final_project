from fastapi import APIRouter, Depends
import threading

from src.services.utils.models_clearing import CleaningService
from src.api.ml import trained_models
from src.core.settings import settings

router = APIRouter(
    prefix='/cleaning',
    tags=['cleaning']
)


@router.on_event("startup")
def start():
    cleaning_service = CleaningService()
    task = threading.Thread(target=cleaning_service.models_cleaning, args=[trained_models, settings.model_expire_seconds])
    task.start()
