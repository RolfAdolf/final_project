import pandas as pd

import requests
from io import StringIO
import base64

from dsh.utils.authorize import authorize
from src.core.settings import settings


preprocess_url = f"http://{settings.host}:{settings.port}/ml/predict"


def send_predict_request(file: str, filename: str, username: str, password: str):

    access_token = authorize(username, password)['access_token']

    content_type, content_string = file.split(',')
    decoded = base64.b64decode(content_string)
    file = pd.read_csv(StringIO(decoded.decode('utf-8')), index_col=0)

    headers = {"Authorization": f"Bearer {access_token}"}
    request = requests.post(preprocess_url, files={'file': (filename, file.to_csv(), 'text/csv')}, headers=headers)

    request.raise_for_status()

    data = StringIO(request.text)

    result = pd.read_csv(data, index_col=0)

    return result.to_csv


def get_predict_data(*args, **kwargs):
    try:
        return send_predict_request(*args, **kwargs)
    except requests.exceptions.HTTPError:
        return send_predict_request(*args, **kwargs)
