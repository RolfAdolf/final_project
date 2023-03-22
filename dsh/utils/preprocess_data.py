from dash import dcc
import pandas as pd

import requests
from io import StringIO
import base64

from dsh.utils.authorize import authorize

preprocess_url = "http://localhost:11000/ml/preprocess"


def preprocess_data(file: str, filename: str, username: str, password: str):
    access_token = authorize(username, password)['access_token']

    content_type, content_string = file.split(',')
    decoded = base64.b64decode(content_string)
    file = pd.read_csv(StringIO(decoded.decode('utf-8')), index_col=0)

    headers = {"Authorization": f"Bearer {access_token}"}
    request = requests.post(preprocess_url, files={'file': (filename, file.to_csv(), 'text/csv')}, headers=headers)
    data = StringIO(request.text)

    result = pd.read_csv(data, index_col=0)
    return result.to_csv
