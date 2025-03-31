import requests

url = "http://127.0.0.1:5000/translate"
data = {
    "text": "I love coding!",
    "target_language": "fr"
}

response = requests.post(url, json=data)
print(response.json())
