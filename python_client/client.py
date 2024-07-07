import requests

endpoints="http://127.0.0.1:8000/challenge2/list"
response = requests.get(endpoints)
print(response.json())