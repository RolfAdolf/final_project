from fastapi import APIRouter

from src.api import users
from src.api import operations
from src.api import ml
from src.api import cleaning


router = APIRouter()

router.include_router(users.router)
router.include_router(operations.router)
router.include_router(ml.router)
# router.include_router(cleaning.router)
