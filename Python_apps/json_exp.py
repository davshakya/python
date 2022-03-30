import json
d={"s":3,"b":6}
j=json.dumps(d)
print(j)

d1='{"s":3,"b":6}'
j1=json.loads(d1)
print(j1)
for i in j1:
    print(i,j1[i])

print(j1["b"])


