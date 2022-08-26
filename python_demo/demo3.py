# # import json

# # with open('D:\demo\payload.json', 'r') as file:
# #     data = json.load(file)
# # print(type(data))

# d={"a":1,"b":2,"c":3}
# for key,value in d.items():
#     if key=="a" or key=="b":
#         print(value)


from datetime import timedelta
from datetime import datetime
x = datetime.now() + timedelta(minutes=10)

print(x)

