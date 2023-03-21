import threading

from src.services.utils.models_clearing import CleaningService
from src.api.ml import trained_models
from src.core.settings import settings


cleaning_service = CleaningService()


def start():
    task = threading.Thread(
        target=cleaning_service.models_cleaning,
        args=[trained_models, settings.model_expire_seconds],
    )
    task.start()


def stop():
    cleaning_service.delete_all()
