import requests

url = "http://127.0.0.1:5000/predict"
data = {"email": "Earn $5000 a day working from home. Join our investment program today!"}
response = requests.post(url, json=data)
print(response.json())
