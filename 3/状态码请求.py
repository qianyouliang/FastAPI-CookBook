import requests
url = 'http://127.0.0.1:8009/items/' 
data = {
    'name':'giserliu'
}
res = requests.post(url,json=data) 
print(res.status_code)
print(res.text)