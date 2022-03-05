a=[2,4,3,'t',7,5,6]
b=[9,6,4,8,3]
# print(a[2])
# a[2]="x"
# print(a[2])
# print(len(a))

# for i in a:
#     print(i, end='')

# print(a[0::-1]) 

# var= "James Bond"
# print(var[::-1])

# a.append(3)
# print(a)

# a.extend(b)
# print(a)

# a.insert(2,55)
# print(a)

# a.pop()
# print(a)

# a.pop(2)
# print(a)

# a.remove(2)
# print(a)

# a.clear()
# print(a)

# a.reverse()
# print(a)

# a.count(10)
# print(a.count(2))

# b.sort()
# print(b)

# b.sort(reverse=True)
# print(b)

# my_list = ["Hello", "Python"]
# print("-".join(my_list))

# sampleList = [10, 20, 30, 40]
# del sampleList[0:6]
# print(sampleList)
lst=[12,15,3,11,1,2,2,3,4,5,6,7,8,5,4,3,2,1,1,4]
# sum=int(lst[0])+int(lst[1])+int(lst[2])+int(lst[3])
# print(sum)
k=0
# print(len(lst))
for i in range(len(lst)):
    k=int(lst[i])+k
    if i==(len(lst)-1):
        print(k)
print(sum(lst))