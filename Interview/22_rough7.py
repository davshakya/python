from itertools import permutations 
your_str ="abcdefghijklmnopqrstuv"
r=11
print("Input string", your_str) 
permutation = permutations(your_str,r)
# print(tuple(permutation)) 
x=tuple(permutation)
print(x[1])
# for m in range (len(x)):
#     str1 ='+'.join(x[m])
#     # print(str1)
#     a	=	1
#     b	=	1
#     c	=	1
#     d	=	1
#     e	=	1
#     f	=	1
#     g	=	1
#     h	=	1
#     i	=	1
#     j	=	1
#     k	=	1
#     l	=	2
#     m	=	2
#     n	=	2
#     o	=	2
#     p	=	2
#     q	=	2
#     r	=	2
#     s	=	2
#     t	=	2
#     u	=	2
#     v	=	2
#     y=eval(str1)
#     if(y==15 or y==18):
#         z = str1.replace("+", "")
#         str2 ='+'.join(z)
#         # print(z)
#         a	=	1
#         l	=	1
#         b	=	2
#         c	=	2
#         d	=	2
#         e	=	2
#         m	=	2
#         n	=	2
#         o	=	2
#         p	=	2
#         f	=	3
#         g	=	3
#         q	=	3
#         r	=	3
#         h	=	4
#         i	=	4
#         j	=	4
#         k	=	4
#         s	=	4
#         t	=	4
#         u	=	4
#         v	=	4
#         csum=eval(str2)
#         if(csum==29 or csum==36):
#             z = str1.replace("+", "")
#             str3 ='+'.join(z)
#             # print(z)
#             a	=	8.5
#             b	=	8.5
#             c	=	8.5
#             d	=	11
#             e	=	10
#             f	=	9.5
#             g	=	9
#             h	=	9
#             i	=	8.5
#             j	=	8.5
#             k	=	8.5
#             l	=	8
#             m	=	9.5
#             n	=	9
#             o	=	8
#             p	=	9
#             q	=	9
#             r	=	8.5
#             s	=	8
#             t	=	8
#             u	=	8
#             v	=	8
#             w=eval(str3)
#             if(w<100):
#                 print(z)