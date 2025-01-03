import requests
from flask import Flask

url = "http://127.0.0.1:5000/predict"
data = {"email": "hiiii"}
response = requests.post(url, json=data)
print(response.json())
