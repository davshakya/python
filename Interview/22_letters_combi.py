from itertools import permutations 
your_str ="abcdefghijklmnopqrstuv"
r=11
print("Input string", your_str) 
permutation = [''.join(x) for x in permutations(your_str,r)] 
# print(tuple(permutation)) 
x=tuple(permutation)

for m in range (len(x)):
    str1 ='+'.join(x[m])
    a	=	1
    b	=	1
    c	=	1
    d	=	1
    e	=	1
    f	=	1
    g	=	1
    h	=	1
    i	=	1
    j	=	1
    k	=	1
    l	=	2
    m	=	2
    n	=	2
    o	=	2
    p	=	2
    q	=	2
    r	=	2
    s	=	2
    t	=	2
    u	=	2
    v	=	2
    y=eval(str1)
    if(y==15 or y==18):
        z = str1.replace("+", "")
        str2 ='+'.join(z)
        # print(z)
        a	=	8
        b	=	8
        c	=	8
        d	=	9
        e	=	9
        f	=	9
        g	=	9
        h	=	10
        i	=	10
        j	=	10
        k	=	10
        l	=	8
        m	=	8
        n	=	8
        o	=	9
        p	=	9
        q	=	9
        r	=	9
        s	=	10
        t	=	10
        u	=	10
        v	=	10
        w=eval(str2)
        if(w<94):
            # print(z)
            f=open("davshakya.txt", "a+")
            a=f.write(str(z))
            a=f.write("\n")

file = open("davshakya.txt","r") 
Counter = 0
Content = file.read() 
CoList = Content.split("\n") 
for i in CoList: 
    if i: 
        Counter += 1
print("Total combination after filter>>  ",Counter)

