$body = '{"text": "今天的风很轻，适合把想法写下来"}'
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/api/analyze" -Body $body -ContentType "application/json"