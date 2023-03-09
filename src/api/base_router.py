from fastapi import APIRouter
from src.api import users
from src.api import operations
from src.api import ml

router = APIRouter()
router.include_router(users.router)
router.include_router(operations.router)
router.include_router(ml.router)
