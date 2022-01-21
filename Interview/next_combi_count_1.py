from itertools import permutations 
your_str ="abcde"
permutation = [''.join(x) for x in permutations(your_str)] 
# print(tuple(permutation)) 
x=tuple(permutation)
# print(x)
# print(len(x))
 
your_str1 ="vwxyz"
permutation = [''.join(y) for y in permutations(your_str1)] 
# print(tuple(permutation))
y=tuple(permutation)
# print(y)
# print(x[1]+y[1])
for (i, j) in zip (x, y):
    m=i,j
    p=''.join(m)
    # print(i,j)
    print(p)
    for k in range (len(p)):
        your_str =k[1]
        r=5
        print("Input string", your_str) 
        permutation = [''.join(w) for w in permutations(your_str,r)] 
        # print(tuple(permutation)) 
        m=tuple(permutation)
        print(m[1])






#   f=open("davshakya.txt", "a+")
#     a=f.write(str(p))
#     a=f.write("\n")

# file = open("davshakya.txt","r") 
# Counter = 0
# Content = file.read() 
# CoList = Content.split("\n") 
# for i in CoList: 
#     if i: 
#         Counter += 1
# print("Total combination after filter>>  ",Counter)





    