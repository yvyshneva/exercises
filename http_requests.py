import requests

response = requests.get('https://www.google.com')

print(response.text[:300])
# <!doctype html><html itemscope=""

response = requests.get('https://www.google.com', stream=True)
print(response.raw.read()[:100])
# b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\

response.request.headers['Accept-Encoding']
# 'gzip, deflate'

response.headers['Content-Encoding']
# 'gzip'

response.ok
# True

response.status_code
# 200

response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))

# or use the Response.raise_for_status() method, which will raise an HTTPError exception only if the response wasn’t successful. 
response = requests.get(url)
response.raise_for_status()

p = {"search": "grey kitten",
    "max_results": 15}
response = requests.get("https://example.com/path/to/api", params=p)
response.request.url
# 'https://example.com/path/to/api?search=grey+kitten&max_results=15'

# POST
p = {"description": "white kitten",
     "name": "Snowball",
     "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)
response.request.url
# 'https://example.com/path/to/api'

response.request.body
# 'description=white+kitten&name=Snowball&age_months=6'

response = requests.post("https://example.com/path/to/api", json=p)
response.request.url
# 'https://example.com/path/to/api'
response.request.body
# b'{"description": "white kitten", "name": "Snowball", "age_months": 6}'
