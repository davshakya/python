import re
cricket_score="Sachin scores 76#$%456%^&* and Dravid scores 40@#$% and Rohit scores 88 and Dhone scores 998672345#$%345#$% Rohit "

# scores=re.findall(r"\d[0-9]*",cricket_score)
# scores=re.findall(r"\W+[^\w]",cricket_score)
# name=re.findall(r"\W[A-Z][a-z]*",cricket_score)
# print(scores)
# print(name)


# x=re.finditer("Rohit",cricket_score)
# for i in x:
#     print(i.span()) 

# s2="Rat Cat Pat Mat Rat Sat"
# match_string=re.findall(r'[^RCPM]at',s2)
# match_string2=re.findall(r'[RCPM]at',s2)
# match_string3=re.findall(r'[A-M]at',s2)
# match_string4=re.findall(r'[^A-M]at',s2)
# # print(match_string4)
# replace_name=re.compile(r"[R]ohit")
# name_new=replace_name.sub("Rajat",cricket_score)
# print(name_new)

ip="155.255.205.255"
x=[]
for i in ip.split("."):
    if  int(i)>=0 and int(i)<=255:
        pass
    else:
        x.append("Invalid")
reg=re.search(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip)
if reg:
    pass
else:
    x.append("Invalid")

if "Invalid" in x:
    print("IP is invalid")
else:
    print("IP is valid")
    


