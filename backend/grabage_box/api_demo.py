import requests

# resp = requests.get("https://api.ipify.org?format=json")
# resp = requests.get("https://zkillboard.com/api/version/")
resp = requests.get("http://localhost:8000/api/profile")
print(resp.json())
