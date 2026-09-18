import urllib.request
import json

data = json.dumps({"text": "hello"}).encode('utf-8')
req = urllib.request.Request('http://localhost:8000/api/analyze', data=data, headers={'Content-Type': 'application/json'})
try:
    resp = urllib.request.urlopen(req)
    print(resp.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")