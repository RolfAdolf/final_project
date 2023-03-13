import requests

url = 'http://localhost:11000/users/authorize'
myobj = {"grant_type": "", "username": "admin", "password": "admin", "scope": "", "client_id": "", "client_secret": ""}


result = requests.post(url, data=myobj)

print(result.text)
