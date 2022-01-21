a={2,4,6,3,2,8}
b={}
print(a)
print(type(b))
b=set(b)
print(type(a))
print(type(b))
b.add(4)
b.add(6)
b.add((7,9,8)) #tuple can be use within set
# b.remove(6)
b.pop()
# b.clear()
print(b)


