from fastapi import Depends

from datetime import datetime
import time
from typing import Dict, List

from src.models.model import Model
from src.db.db import Session


class CleaningService:
    def __init__(self):
        self.session = Session()

    def extract_ids_date(self) -> List[Model]:
        models = self.session.query(Model.id, Model.created_at).all()
        return models

    def delete_ids(self, ids: List):
        models = (self.session.query(Model).filter(Model.id.in_(ids))).delete()
        self.session.commit()

    def delete_all(self):
        models = (self.session.query(Model)).delete()
        self.session.commit()

    def models_cleaning(self, trained_models: Dict, model_expire_time: int = 60 * 10):
        while True:
            models = self.extract_ids_date()
            datetime_ = datetime.utcnow()

            black_list = []

            for model in models:
                if (
                    self.time_difference(model.created_at, datetime_)
                    > model_expire_time
                ):
                    black_list.append(model.id)
                    trained_models.pop(model.id, None)

            self.delete_ids(black_list)

            print(f"Deleting models with ids: {black_list}")
            time.sleep(model_expire_time)

    @staticmethod
    def time_difference(earlier_time: datetime, later_time: datetime):
        return (later_time - earlier_time).seconds
