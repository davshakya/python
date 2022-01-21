from itertools import permutations 
your_str ="abcdefghij"
r=int(input("Enter Your number\n"))
print("Input string", your_str) 
permutation = [''.join(x) for x in permutations(your_str,r)] 
# print(tuple(permutation)) 
x=tuple(permutation)
print(x[1:3])

# for m in range (len(x)):
#     str1 ='+'.join(x[m])
#     a=1
#     b=1
#     c=1
#     d=1
#     e=1
#     f=2
#     g=2
#     h=2
#     i=2
#     j=2
#     y=eval(str1)
#     if(y==8 or y==7):
#         z = str1.replace("+", "")
#         str2 ='+'.join(z)
#         # print(z[1])
#         a=2
#         b=2
#         c=3
#         d=3
#         e=5
#         f=2
#         g=2
#         h=3
#         i=3
#         j=5
#         w=eval(str2)
#         if(w<12):
#             # print(z[1])
#             f=open("davshakya.txt", "a+")
#             a=f.write(str(z))
#             a=f.write("\n")

# file = open("davshakya.txt","r") 
# Counter = 0
# Content = file.read() 
# CoList = Content.split("\n") 
# for i in CoList: 
#     if i: 
#         Counter += 1
# print("Total combination after filter>>  ",Counter)

