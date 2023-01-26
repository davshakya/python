import json
import requests
url="http://10.20.50.179:9590/httpapi/JsonReceiver"
request_json={
  "json_intf": [
    {
      "ver": "1.0",
      "key": "venkat",
      "encrypt": "2",
      "sch_at": "",
      "messages": [
        {
          "dest": [
            "919500070292"
          ],
          "text": "Gud morning Tanla",
          "template_values": [
            "var1",
            "var2",
            "var3",
            "var4",
            "var4",
            "var5"
          ],
          "send": "alerts",
          "vp": 30,
          "type": "PM",
          "dlt_entity_id": "1234",
          "dlt_template_id": "0001",
          "tag1": "12345",
          "tag2": "12345",
          "tag3": "12345",
          "tag4": "12345",
          "tag5": "12345",
          "urltrack": "",
          "cust_ref": ""
        }
      ]
    }
  ]
}

# print(type(request_json),request_json)

def update_request_json_encrypt(request_json):
        if request_json["json_intf"][0]["encrypt"] == "1":
            for k1, v1 in dict(request_json["json_intf"][0]["messages"][0]).items():
                if k1 == "dest":
                    request_json["json_intf"][0]["messages"][0][k1] = ["test_java_python"]
                elif k1 == "text":
                    request_json["json_intf"][0]["messages"][0][k1] = "test_java_python"
                elif k1 == "send":
                    request_json["json_intf"][0]["messages"][0][k1] = "test_java_python"
                print(k1,v1)
            return request_json

        elif request_json["json_intf"][0]["encrypt"] == "2":
            for i in range(len(request_json["json_intf"][0]["messages"][0]["template_values"])):
                    request_json["json_intf"][0]["messages"][0]["template_values"][i] = "test_java_python"
            for k1, v1 in dict(request_json["json_intf"][0]["messages"][0]).items():
                if k1 == "dest":
                    request_json["json_intf"][0]["messages"][0][k1] = ["test_java_python"]
            for k1, v1 in dict(request_json["json_intf"][0]["messages"][0]).items():
                if not isinstance(request_json["json_intf"][0]["messages"][0][k1],list):
                    request_json["json_intf"][0]["messages"][0][k1] = "test_java_python"
            return request_json

        else:
            return request_json

update_request_json_encrypt(request_json)
print(request_json)

res=requests.post(url,request_json)
r=res.json()
print(r)
