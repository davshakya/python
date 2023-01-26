import json

import requests

url = "https://reqres.in/api/users"

res = requests.post(url)
print(res.json())



payload_file=open("D:\demo\selenium\selenium_demo\data_file.json","r").read()
# payload_file=
# payload_data["name"]="Shakya"
res = requests.post(url, data=json.loads(payload_file))
# print(res)
print(res.json())
# res.json()["name"] = "shakya"
print(res.json()["name"])



# assert res.json()["name"] == "devendra"
