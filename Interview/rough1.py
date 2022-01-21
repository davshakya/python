from itertools import permutations 
ini_str =input("Enter any string>> ")
r=int(input("Enter target combination>> "))
print("Initial string", ini_str) 
permutation = [''.join(p) for p in permutations(ini_str,r)] 
print(tuple(permutation)) 
x=tuple(permutation)

for j in range (len(x)):
    str1 ='+'.join(x[j])
    a=8.5
    b=8.5
    c=9
    d=9
    e=9.5
    f=9.5
    g=10
    h=10
    i=10.5
    j=10.5
    k=11
    l=11
    m=11
    n=11.5
    o=12
    p=12
    q=12.5
    r=12.5
    s=13
    t=13
    u=13.5
    v=13.5
    y=eval(str1)
    if(y<48):
        # print(*str1)
        print(f"{str1}=",y)
# print("Total Combination is =",len(str1))



