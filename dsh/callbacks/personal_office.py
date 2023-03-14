import requests
import jwt
import json

from src.core.settings import settings

download_url = 'http://localhost:11000/ml/download_data'


def download_data(access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    request = requests.get(download_url, headers=headers)
    print(request)
    print(request.text)
