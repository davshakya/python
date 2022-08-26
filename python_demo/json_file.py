from codecs import utf_16_be_decode
import json
with open('payload.json') as f:
   data = json.load(f)
# print(data)

md=data["messages"][0]
# print(md)
# print(md.keys())

for key,value in md.items():
    if key == "dest" or key=="tag1":
            if isinstance(value, list):
                value="tiger"
            md.update({key: value})
        
    # print(key,value)
    # print(md.items())
print(data)

# for key in md:
#     print(key)

