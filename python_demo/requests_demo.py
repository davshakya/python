import requests
import json

url = "https://reqres.in/api/users?page=2"
url_put="https://reqres.in/api/users/2"
# payload = { "name": "Devendra","job": "leader"}

# resp = requests.post(url, data=payload)
# resp_json = resp.json()
# print(resp_json)

# payload = { "name": "manan","job": "leader"}
# resp=requests.put(url_put,data=payload)
# print(resp)
# resp_json = resp.json()
# print(resp_json)

payload = {"job": "tester"}
resp=requests.patch(url_put,data=payload)
resp_json = resp.json()
print(resp_json)


# r=requests.get(url)
# print(r.headers)
# print(r.text)
# print(r.content)
# print(r.cookies)
# print(r.history)
# print(r.json())
#
# json_response=r.json()
# code=r.status_code
# assert code == 200
# print(type(json_response),json_response)
# page=json_response["data"][0]
# print(page)
