import pandas as pd

import requests
from io import StringIO

from src.core.settings import settings

download_url = f"http://0.0.0.0:8000/ml/download_data"


def send_download_request(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    request = requests.get(download_url, headers=headers)
    request.raise_for_status()
    data = StringIO(request.text)
    return pd.read_csv(data, index_col=0).to_csv


def download_data(*args, **kwargs):
    try:
        return send_download_request(*args, **kwargs)
    except requests.exceptions.HTTPError:
        return send_download_request(*args, **kwargs)
