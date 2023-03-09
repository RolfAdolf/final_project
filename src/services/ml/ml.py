from typing import List, Optional, TypeVar, Tuple
from fastapi import Depends
from datetime import datetime

from src.db.db import get_session
from src.models.model import Model
from src.models.schemas.model.model_request import ModelRequest
from src.services.ml.preprocess import full_preprocess
from src.services.ml.train import train, ScikitModel


PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')


class TrainedModel:
    def __init__(self,
                 trained_model: ScikitModel,
                 trained_scaler: Optional[object] = None
                 ):
        self.model = trained_model
        self.scaler = trained_scaler


class MLService:
    def __init__(self, session=Depends(get_session)):
        self.session = session

    @staticmethod
    def preprocess(data: PandasDataFrame) -> PandasDataFrame:
        return full_preprocess(data)

    @staticmethod
    def train(data: PandasDataFrame, model_type: str) -> TrainedModel:
        training_result = train(model_type, data)
        model, scaler = list(training_result.values())
        return TrainedModel(model, scaler)

    def all(self):
        models = (
            self.session
            .query(Model)
            .order_by(
                Model.id.desc()
            )
            .all()
        )
        return models

    def all_user_models(self, user_id: int):
        models = (
            self.session
            .query(Model)
            .filter(
                Model.created_by == user_id
            )
            .all()
        )
        return models

    def add(self,
            model_schema: ModelRequest,
            created_user_id: int
            ) -> Model:
        datetime_ = datetime.utcnow()
        model = Model(
            **model_schema.dict(),
            created_at=datetime_,
            created_by=created_user_id
        )
        self.session.add(model)
        self.session.commit()
        return model
