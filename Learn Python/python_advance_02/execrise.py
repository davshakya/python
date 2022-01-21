# l=[str(i*7)  for i in range (1,11)]
# print(l)
# k="\n".join(l)
# print(k)

from functools import reduce
l=[12,23,13,45,33,76,90]
a=reduce(max,l)
print(a)

