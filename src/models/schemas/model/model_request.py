from typing import Literal
from pydantic import BaseModel


class ModelRequest(BaseModel):
    model_type: Literal['SVM', 'Log_Reg', 'XGB', 'Forest']
