import requests
import json

endpoint_file = open("D:\\demo\python\\Learn Python\\json_file.json", "r").read()
end_dict = json.loads(endpoint_file)
print(end_dict)