import requests
from flask import Flask

url = "http://127.0.0.1:5000/nhanle"
data = {"email": "Subject: enron methanol ; meter  : 988291 this is a follow up to the note i gave you on monday , 4... "}
response = requests.post(url, json=data)
print(response.json())
