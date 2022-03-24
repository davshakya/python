from re import L


l=["2","4","5"]
n=list(map(int,l))
n=list(map(lambda x:x*x,n))
print(n)
print(sum(n))
l=[2,4,5]

print([item for item in l if item%2==0])







