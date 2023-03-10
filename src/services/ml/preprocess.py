import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from typing import TypeVar, Tuple, Optional, Dict

PandasDataFrame = TypeVar('pandas.core.frame.DataFrame')


def convert_types(data: PandasDataFrame) -> PandasDataFrame:
    data['Process temperature [K]'] = pd.to_numeric(data['Process temperature [K]'])
    data['Rotational speed [rpm]'] = pd.to_numeric(data['Rotational speed [rpm]'])
    data['Torque [Nm]'] = pd.to_numeric(data['Torque [Nm]'])
    data['Tool wear [min]'] = pd.to_numeric(data['Tool wear [min]'])
    if 'Target' in list(data.columns):
        data['Target'] = pd.to_numeric(data['Target'])
    return data


def drop_extra_columns(data: PandasDataFrame) -> PandasDataFrame:
    columns = [list(data.columns)[0], 'Product ID', 'Air temperature [K]']
    if 'Failure Type' in data.columns:
        columns.append('Failure Type')
    return data.drop(columns=columns)


def categorical_processing(data: PandasDataFrame) -> PandasDataFrame:
    cat_features = ['Type']
    prefixes = ['type']
    return pd.get_dummies(columns=cat_features, data=data, prefix=prefixes)


def full_preprocess(data: PandasDataFrame) -> PandasDataFrame:
    return categorical_processing(drop_extra_columns(data))


def feature_target_return(data: PandasDataFrame) -> Tuple[PandasDataFrame]:
    x = data.loc[:, data.columns != 'Target'].values
    y = data['Target'].values
    return x, y


def scaler_return(
        train: np.ndarray
        ):
    scaler = StandardScaler()
    scaler.fit(train)
    return scaler


def train_return(
        train_data: PandasDataFrame,
        normalizing: bool = True
        ) -> Dict:
    x, y = feature_target_return(train_data)
    if normalizing:
        scaler = scaler_return(x)
        x = scaler.transform(x)
    else:
        scaler = None
    return {
        "data": (x, y),
        "scaler": scaler
    }


def train_test_return(
        train: PandasDataFrame,
        test_size_proportion: float,
        normalizing: bool = True
        ) -> Dict:

    x, y = feature_target_return(train)
    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y,
                                                        stratify=y,
                                                        test_size=test_size_proportion
                                                        )
    if normalizing:
        scaler = scaler_return(x_train)
        x_train, x_test = scaler.transform(x_train), scaler.transform(x_test)
    else:
        scaler = None
    return {
        "data": (x_train, x_test, y_train, y_test),
        "scaler": scaler
    }

def test_return(
        test: PandasDataFrame
) -> np.ndarray:
    x = test.loc[:, test.columns != 'Target'].values
    return x
