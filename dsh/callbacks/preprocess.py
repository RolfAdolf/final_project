import pandas as pd

import requests
from io import StringIO

from src.core.settings import settings


download_url = "http://localhost:11000/ml/download_data"


def download_data(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    request = requests.get(download_url, headers=headers)

    # s = str(request.content, 'utf-8')
    data = StringIO(request.text)

    return pd.read_csv(data, index_col=0).to_csv
