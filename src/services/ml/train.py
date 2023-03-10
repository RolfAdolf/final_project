from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from xgboost import XGBClassifier

from typing import Protocol, TypeVar

from src.services.ml.preprocess import train_return, train_test_return

models = {
    "SVM": SVC,
    "Log_Reg": LogisticRegression,
    "XGB": XGBClassifier,
    "Forest": BaggingClassifier
}

PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')


class ScikitModel(Protocol):
    def fit(self, x, y, sample_weight=None): ...
    def predict(self, x): ...
    def score(self, x, y, sample_weight=None): ...
    def set_params(self, **params): ...


def train(
        model_type: str,
        train_data: PandasDataFrame,
        test_split: float = 0.0,
        normalizing: bool = True
        ):

    model = models[model_type]

    if test_split == 0:
        train_data = train_return(train_data, normalizing)
        x, y = train_data["data"]
    else:
        train_data = train_test_return(train_data, test_split, normalizing)
        x_train, x_test, y_train, y_test = train_data["data"]
    scaler = train_data["scaler"]

    svc_params = {'C': [1] + [10*i for i in range(1, 10)]}

    if test_split == 0:
        model = GridSearchCV(model(), svc_params).fit(x, y)
    else:
        model = GridSearchCV(model(), svc_params).fit(x_train, y_train)
    return {
        "model": model,
        "scaler": scaler
    }
