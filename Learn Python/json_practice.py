import requests
import json


logindata={"email": "loveleen.gandhi@builder.ai", "password": "12345678"}
data_json=json.dumps(logindata)
url="https://api-staging-pmdashboard.engineer.ai/api/v1/pm/sessions/sign_in"
headers_data={"Accept":"application/json", "Content-Type":"application/json","partner-code":"e-ai"}
response = requests.request("POST", url, headers=headers_data, data=data_json)
response_dict=response.json()
print("#####",response_dict)
print(response_dict["data"]["auth-token"])

