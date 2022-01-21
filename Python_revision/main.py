# x,y=4,5
# print(x,y)
# y,x=x,y
# print(x,y)

# print("Devendra",end=" ")
# print("Singh", "Shakya ",sep='$')
# print("From Orai")

# a=input("Enter you name: ")
# print(a)

lst=[12,15,3,10]
sum=int(lst[0])+int(lst[1])+int(lst[2])+int(lst[3])
# print(sum)
k=0
for i in range(len(lst)):
	k=int(lst[i])+k
    if i==len(lst):
        print(k)