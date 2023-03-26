import pandas as pd

import requests
from io import StringIO
import base64

from dsh.utils.authorize import authorize
from src.core.settings import settings


preprocess_url = f"http://0.0.0.0:8000/ml/train_model"


def send_data_to_train(
    file: str, filename: str, model_type: str, username: str, password: str
):
    access_token = authorize(username, password)["access_token"]

    params = {"model_type": model_type}

    content_type, content_string = file.split(",")
    decoded = base64.b64decode(content_string)
    file = pd.read_csv(StringIO(decoded.decode("utf-8")), index_col=0)

    headers = {"Authorization": f"Bearer {access_token}"}
    request = requests.post(
        preprocess_url,
        files={"file": (filename, file.to_csv(), "text/csv")},
        headers=headers,
        params=params,
    )
    request.raise_for_status()


def train_model_request(*args, **kwargs):
    try:
        send_data_to_train(*args, **kwargs)
    except requests.exceptions.HTTPError:
        send_data_to_train(*args, **kwargs)
