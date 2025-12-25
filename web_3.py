import requests

url = "http://127.0.0.1:8000/post"

payload = {
    "title":"Greeting",
    "content":"Welcome to Python"
}

response = requests.post(url=url,data=payload)
print(response.text)