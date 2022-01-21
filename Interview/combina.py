# def cmb(x, y):
#     if not x: 
#         return
#     y.add(x)
#     for i in range(0, len(x)):
#         t = x[0:i] + x[i + 1:]
#         cmb(t,y)
# y = set()
# cmb("abcdefghij", y) 
# print(y)

# a	=	2
# b	=	3
# c	=	4
# d	=	5
# e	=	6
# f	=	7
# g	=	8
# h	=	9
# i	=	10
# j	=	11
# def cmb(x, y):
#     if not x: 
#         return
#     y.add(x)
#     for z in range(0, len(x)):
#         t = x[0:z] + x[z + 1:]
#         cmb(t,y)
# y = set()
# cmb("abcdefghij", y) 
# t=list(y)

# def words_to_marks(s):
     
#     word_list = list(s)
#     a_z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#     sum = 0
#     for w in word_list:
#         sum += a_z.index(w) + 1
#     return sum
# print()


# def cmb(x, y):
#     if not x: 
#         return
#     y.add(x)
#     for z in range(0, len(x)):
#         t = x[0:z] + x[z + 1:]
#         cmb(t,y)       
# y = set()
# cmb("123", y) 
# t=list(y)
# # print(t[1])

# # print(len(t))
# for i in range (len(t)):
#  j=str(t[i])
# # print(j)
# 
# def sum_str(str1):
#         sum_dgt = 0
#         for x in str1:
#             if x.isdigit() == True:
#                 z = int(x)
#                 sum_dgt = sum_dgt + z
#         return sum_dgt  
# print(sum_str("a1234"))



# x = a b c
# x = txt.replace(",", "+")
# y=eval(x)
# print(y)

# import itertools
# def comb():
#     values = "abcdefghij"
#     com = itertools.combinations_with_replacement(values, 3)
#     for val in com:
#         print()
#         print('"',*val,end='"' )
# m=comb()
# print(m)

# txt =m
# a=2
# b=3
# c=4
# d=5
# e=6
# f=7
# g=8
# h=9
# i=10
# j=11
# x = txt.replace(" ", "+")
# y=eval(x)
# print(y)

import itertools
values = "abcdefghijklmnopqrtuv"
com = itertools.combinations_with_replacement(values, 11)
for val in com:
    # print('"',*val,end='"')
    print(*val)

# txt =
# a=2
# b=3
# c=4
# d=5
# e=6
# f=7
# g=8
# h=9
# i=10
# j=11
# x = txt.replace(" ", "+")
# y=eval(x)
# print(y)
# 
# t=list(permute(my_nums))
# for i in range (len(t)):
#  j=str(t[i])
#  def sum_str(str1):
        # sum_dgt = 0
        # for x in str1:
            # if x.isdigit() == True:
                # z = int(x)
                # sum_dgt = sum_dgt + z
        # return sum_dgt
#  m=sum_str(t[i])
#  print(m)