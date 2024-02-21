import http.client
import json

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/golf/trial/v3/en/players/wgr/2024/rankings.json?api_key=4dmquyjjhaqcahf3934sqhzz")

res = conn.getresponse()
data = res.read()

print(json.loads(data.decode("utf-8")))