import requests

url = "http://127.0.0.1:5000/classify"
data = {'email': 'Chúc mừng bạn! Thành công rồi nè'}

response = requests.post(url, json=data)
print(response.json())
