import requests
import jwt
import json

from src.core.settings import settings

url = "http://localhost:11000/users/authorize"


def authorize(login: str, password: str):
    obj = {
        "grant_type": "",
        "username": login,
        "password": password,
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }

    query_result = requests.post(url, data=obj)
    query_result.raise_for_status()

    access_token = json.loads(query_result.text)["access_token"]
    payload = jwt.decode(
        access_token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
    )
    username = payload.get("context").get("user").get("username")
    role = payload.get("lvl")

    return {"access_token": access_token, "username": username, "role": role}
