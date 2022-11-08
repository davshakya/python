n=input("Enter any number=")
i=0
l=[]
for i in range(len(n)):
    x=l.append(int(n[i])**len(n))
if sum(l)==int(n):
    print("It is armstrong number")
else:
    print("It not armstrong")





