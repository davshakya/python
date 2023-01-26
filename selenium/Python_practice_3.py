import sympy.testing.runtests

ls = [34, 25, 5, 6, 9, 12]
# k=ls.copy()
#
ls1 = [3, 54, 2, 54, 44]
# l=[]
# for i in range(1,len(ls)+1):
#     l.append(ls[-i])
# print(l)
# ls.extend(ls1)
# ls.append(90)
# ls.insert(1,30)
# print(ls)
# del ls[2]
# ls.remove(30)
# ls.pop(5)
# print(ls)
# print(k)
# l=list(map(lambda x:x*x,ls))
l1 = ["a", "b", "c"]
l2 = ["x", "y", "z"]
# rl=[]
# for i in l1:
#     for j in l2:
#         rl.append(i+j)
# print(rl)

# res=[i+j for i in l1 for j in l2]
# print(res)

# for i,j in zip(l1,l2):
#     print(i,j)
#
# print(list(zip(l1,l2)))

# for i in zip(l1,l2):
#     print(i)

lt = ["Dev", "Sha", "*", "man"]
# for i in lt:
#     if not(len(i)==0):
#         print(i)
# k = list(filter(lambda x: x != "*", lt))
# print(k)

# lt1 = [5, 20, 20, 4, 2, 2, 6, 7, 8, 6]
# for i in lt1:
#     if lt1.count(i) >= 2:
#         lt1.remove(i)
# print(lt1)

# s1="Atuley"
# s2="Dev"
# m=int(len(s1)/2)
# print(s1[:m]+s2+s1[m:])

s1 = "P@#yn26at^&i5ve"
# #
# num_count=0
# alpha_count=0
# symbol_count=0
#
# for i in s1:
#   if i.isdigit():
#      num_count=num_count+1
#      print(i)
#
#   elif i.isalpha():
#      alpha_count=alpha_count+1
#   else:
#      symbol_count=symbol_count+1
#      print(i)
# print("num_count :",num_count)
# print("alpha_count :",alpha_count)
# print("symbol_count :",symbol_count)

#
# l=[42,4,424678,3]
# print(sorted(l))
# # l.sort()
# # print(l)
# print(s1.lower())
import re
s1 = "P@#yn26at^&i5ve"
# x=re.findall(r'\d',s1)
# x=re.findall(r'[\w]',s1)
# x=re.findall(r'[\W]',s1)
# x=re.findall(r've\Z',s1)
# x=re.findall(r'[a-zA-Z]',s1)
# x=re.findall(r'[a-z]',s1)
# x=re.findall(r'[A-Z]',s1)

# print(x)
# i=[int(j) for j in x]
# print(sum(i))
print(s1.join("-"))
