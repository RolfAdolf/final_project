import requests


url = 'http://localhost:11000/users/authorize'


def authorize(
    username: str,
    password: str
):
    obj = {"grant_type": "", "username": username, "password": password, "scope": "", "client_id": "",
             "client_secret": ""}
    return requests.post(url, data=obj)

