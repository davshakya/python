from requests import *
import requests
import json
url="http://10.20.50.179:9590/httpapi/JsonReceiver"
mydata=open("D:\demo\python_demo\payload.json","r").read()
r=requests.post(url,mydata)
r_json=r.json()
print(r_json["ackid"])
# print(r.status_code)
# print(r.content)
# print(r.url)
assert r.status_code==200

