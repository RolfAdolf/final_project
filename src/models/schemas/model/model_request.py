from typing import Literal
from pydantic import BaseModel
from enum import Enum


class ModelType(str, Enum):
    SVM = "SVM"
    Log_Reg = "Log_Reg"
    XGB = "XGB"
    Forest = "Forest"


class ModelRequest(BaseModel):
    model_type: ModelType
