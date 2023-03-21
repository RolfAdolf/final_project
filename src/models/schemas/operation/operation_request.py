from typing import Literal
from pydantic import BaseModel
from enum import Enum


class OperationType(str, Enum):
    preprocess = "preprocess"
    train = "train"
    predict = "predict"
    download = "download"


class OperationRequest(BaseModel):
    operation: OperationType
