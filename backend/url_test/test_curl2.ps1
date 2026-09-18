$url = "http://localhost:8000/api/analyze"
$body = '{"text": "今天的风很轻"}'
$params = @{
    Uri = $url
    Method = "POST"
    Body = $body
    ContentType = "application/json"
}
Invoke-RestMethod @params