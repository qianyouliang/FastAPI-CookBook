import requests
url = 'http://127.0.0.1:8009/user/' 
data = {
    "username": "Foo",
    "password": "1234321",
    "email": "example@example.com"
}
res = requests.post(url, json=data) 
print(res.json())