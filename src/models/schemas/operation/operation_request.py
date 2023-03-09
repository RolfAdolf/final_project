from typing import Literal
from pydantic import BaseModel


class OperationRequest(BaseModel):
    operation: Literal['preprocess', 'train', 'predict', 'download']
