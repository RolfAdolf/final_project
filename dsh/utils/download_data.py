import pandas as pd

import requests
from io import StringIO


download_url = "http://localhost:11000/ml/download_data"


def download_data(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    request = requests.get(download_url, headers=headers)

    data = StringIO(request.text)

    return pd.read_csv(data, index_col=0).to_csv
