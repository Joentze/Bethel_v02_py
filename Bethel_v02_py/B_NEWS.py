import requests as req 
import json 

API_key = 'e72ed87ee0bb41edb4ed2b146d8a3011'
query = 'south china sea'
search_url = 'https://api.cognitive.microsoft.com/bing/v5.0/news/search'

headers = {"Ocp-Apim-Subscription-Key" : API_key}
params  = {"q": query, "textDecorations": True, "textFormat": "HTML","count":"100"}

response = req.get(search_url, headers = headers, params=params)
response.raise_for_status()
dump_search_results = json.dumps(response.json())
search_json = json.loads(dump_search_results.strip())
#print(search_json)
cnt = 0
for x in search_json["value"]:
    cnt += 1
    print(cnt)
    print(x["description"].strip()+"/")
