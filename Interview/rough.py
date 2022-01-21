from itertools import permutations 
your_str ="abcdefghij"
r=5
print("Input string", your_str) 
permutation = [''.join(x) for x in permutations(your_str,r)] 
# print(tuple(permutation)) 
x=tuple(permutation)

for m in range (len(x)):
    y=list(permutation[m]) 
    # print(y)
    str1 ='+'.join(y)
    # print(str1)
    a=1
    b=1
    c=1
    d=1
    e=1
    f=2
    g=2
    h=2
    i=2
    j=2
    sum=eval(str1)
    # print(y)
    if(sum==8 or sum==7):
        z = str1.replace("+", "")
        str2 ='+'.join(z)
        # print(str2)
        a=2
        b=2
        c=3
        d=3
        e=5
        f=2ew
        g=2
        h=3
        i=3
        j=5
        w=eval(str2)
        if(w==11):
            rpl = str2.replace("+", "")
            print(rpl)
        
            f=open("davshakya.txt", "a+")
            a=f.write(str(rpl))
            a=f.write("\n")

file = open("davshakya.txt","r") 
Counter = 0
Content = file.read() 
CoList = Content.split("\n") 
for i in CoList: 
    if i: 
        Counter += 1
print("Total combination after filter>>  ",Counter)

