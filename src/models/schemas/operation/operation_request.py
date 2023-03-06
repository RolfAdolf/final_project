from typing import Literal
from pydantic import BaseModel
from datetime import datetime


class OperationRequest(BaseModel):
    method: Literal['preprocess', 'train', 'predict', 'download']
