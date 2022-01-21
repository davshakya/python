import re
txt = "The rain in Spain"
# x = re.search("ai", txt)
x = re.findall("ai", txt)
# x = re.sub("\s","9", txt,2)

print(x)