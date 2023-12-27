import re
st = "davshakya@gmail.com"
# r=re.findall(r'[^\w\s]',st)
#
# r=re.findall(r'\.',st)
# print(r)
# r=re.findall(r'[^MRD]a',st)
# r=re.findall(r'[a-zA-Z]',st)
#
# for i in re.finditer("Manan",st):
#     index=i.span()
#     print(index)
#
#
# r=re.finditer("Manav",st)
# for i in r:
#     print(i.span())

# r=re.findall("dav",st)
# name=re.findall(r'[A-Z][a-z]*',st)
# digit=re.findall(r'\d{3}',st)
# print(name)
# print(digit)

# mark={}
# i=0
# for x in name:
#     mark[x]=digit[i]
#     i=i+1
# print(mark)
#

st2="harry12341 pot765ter"
# match =re.search(r"\Aha",st2)
# match =re.search(r"er\b",st2)
match =re.findall(r"\d[1]{1,4}",st2)

print(match)