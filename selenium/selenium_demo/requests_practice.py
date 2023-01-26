import json

import requests

url = "https://reqres.in/api/users?page=2"

r = requests.get(url)
# r_json = r.text
# r_json = r.content
r_dict = r.json()
r_headers=r.headers
r_sc=r.status_code


print(r_sc)
print(r_headers)
r_json =json.dumps(r_dict)
print(type(r_json))
print(type(r_dict))


