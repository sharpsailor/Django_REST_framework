import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"  # http://127.0.0.1:8000/
get_response = requests.get(
    endpoint, params={"abc": 123}, json={"query": "Hello World"}
)  # HTTP request
# print(get_response.headers)
# print(get_response.text)  # print raw text response
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP REQUEST -> JSON
# JavaScript object Nototion ~ Python Dictionary
print(get_response.json())
