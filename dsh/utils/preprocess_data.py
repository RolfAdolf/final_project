import pandas as pd
import plotly.express as px
import numpy as np

import requests
from io import StringIO
import base64

from dsh.utils.authorize import authorize
from src.core.settings import settings
from src.services.ml.preprocess import PandasDataFrame


preprocess_url = f"http://{settings.host}:{settings.port}/ml/preprocess"


def graph_from_data(df: PandasDataFrame):
    values = [
        np.sum(df['type_H'].values),
        np.sum(df['type_L'].values),
        np.sum(df['type_M'].values)
    ]
    names = [
        'High quality',
        'Low quality',
        'Medium quality'
    ]
    title = 'Distribution of the product quality'
    return px.pie(df, values=values, names=names, title=title)


def send_preprocess_request(file: str, filename: str, username: str, password: str):
    access_token = authorize(username, password)['access_token']

    content_type, content_string = file.split(',')
    decoded = base64.b64decode(content_string)
    file = pd.read_csv(StringIO(decoded.decode('utf-8')), index_col=0)

    headers = {"Authorization": f"Bearer {access_token}"}
    request = requests.post(preprocess_url, files={'file': (filename, file.to_csv(), 'text/csv')}, headers=headers)
    request.raise_for_status()
    data = StringIO(request.text)

    df = pd.read_csv(data, index_col=0)
    return df.to_csv, graph_from_data(df)


def preprocess_data(*args, **kwargs):
    try:
        return send_preprocess_request(*args, **kwargs)
    except requests.exceptions.HTTPError:
        return send_preprocess_request(*args, **kwargs)
