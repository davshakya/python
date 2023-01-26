# from sympy import factorial
# print(factorial(5))

# n=5
# fact=1
# while n>=1:
#     fact=fact*n
#     n=n-1
# print(fact)

# Armstrong Number
# n=153
# s=str(n)
# l=len(s)
# k=0
# for i in range(l):
#     k=k+int(s[i])**l
# print(k)


# for i in range(1,101):
#     p=[]
#     for j in range(1,i+1):
#         if i%j==0:
#             p.append(i)
#     if len(p)==2:
#         print(i)

# n=1
# a=0
# b=1
# z=a+b
# while n<10:
#     a=b
#     b=z
#     z=a+b
#     n=n+1
#     print(z)


# l=["abc",11,2,6,33,7,3,53,2,6,"xyz"]
# lt=[11,2,6,33,7,3,53,2,6]
# l[0],l[-1]=l[-1],l[0]
# l.clear()
# s="devendra"
# print(s[::-1])
# l=l[::-1]
# print(l)

# n=0
# for i in lt: n=n+i
# print(n)

# print(reduce(lambda a,b:a+b,lt))

# lt.sort()
# print(lt[0],lt[-1])
# print(lt[-5:])

# m1=[i for i in lt if i%2==0]
# m2=[i for i in lt if i%2!=0]
# print(m1,m2)

# l=["abc",11,2,6,33,7,3,53,2,6,"xyz"]
# k=l.count(6)
# print(k)

# lt=[11,2,6,33,7,3,53,2,6]
# j=0
# for i in lt:
#     j=i+j
# print(j)

# s=sorted(lt)
# print(s)
# lt.sort()
# print(lt)

# s="malayalam"
# if s==s[ : :-1]:
#     print("It is pelindrome")
# else: 
#     print("not pelindrome")

# s="malayalam"
# k=s.replace("m"," ",1)
# st=s[:2]+s[3:]


# s="Gfg is best . Geeks are good and Geeks like Gfg"
# st=s.count("is")
# print(st)

# if "is" in s:
#  print("Yes")

# if s.count("is")>0:
#     print("Yes")

# from code import interact
# from tkinter import Y

# from pyparsing import java_style_comment


# s="Gfg is best . Geeks are good and Geeks like Gfg"
# for k in s.split():
#     print(k,s.count(k),end=" ")

# d={k:s.count(k) for k in s()}
# print(d)

# st="devendra"
# l=[]
# vowel="aeiou"
# for char in st:
#     if char in vowel:
#         l.append(st)    
# print(set(l))

# st="devendra"
# l=list(st)    
# st=set(l)
# for i in st:
#     print(i,end="")

# s="GeeksForGeeks"
# x=s.isalnum()
# if x==True:
#     print(f"string {s} have Valid charectors.")
# else:
#     print(f"String {s} have spacial charrectors.") 

# s="Geeks For Geeks"
# st=s.split()
# k="-".join(st)
# print(k)

# s= 'geeksforgeeks'
# j=0
# for i in s:
#     k=s.count(i)
#     if k<2:
#         print(i,k)

# s= 'geeksforgeeks'
# a=[] 
# for i in s:
#     k=s.count(i)
#     if k>1:
#         a.append(i)
# print(set(a))

# s= 'geeks for geeks'
# d={k:s.count(k) for k in s.split()}
# print("geeks",d.get("geeks"))


# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# res = []
# [res.append(x) for x in test_list if x not in res]
# print(res)

# test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
# res = []
# for i in test_list:
#     if i not in res:
#         res.append(i)
# print(res)

# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# n=153
# s=str(n)
# k=0
# for i in range(0,len(s)):
#    k=k+int(s[i])**len(s)
# if k==n:
#     print("It is armstrong number")
# else:
#     print("invalid armstrong")

# x=1
# y=1
# z=1
# for i in range(0,10):
#     x=y
#     y=z
#     z=x+y
#     print(z)


# n=0
# x=1
# y=1
# z=1
# while n<10:
#     x=y
#     y=z
#     z=x+y
#     print(z)
#     n=n+1

# n=7
# k=[]
# for i in range(1,n+1):
#     if n%i==0:
#         k.append(i)
# if len(k)==2:
#     print("It is prime")
# else:
#     print("Not prime")


# for i in range(1,101):
#     k=[]
#     for j in range(1,i+1):
#         if i%j==0:
#             k.append(j)
#     if len(k)==2:
#         print(i)        


# for i in range(1,5):
#     print(i*"*")

# n=20
# s=20
# j=0
# for i in range(1,s):
#     print(n*" ",i*"*"+j*"*")
#     n=n-1
#     j=j+1

# num=10
# for i in range(0,10):
#     print(n)
#     num=num-1

# for even in range(1,10):
#     if even%2==0:
#         print(even)

# j=0
# for i in range(0,4):
#     j=j+i**2
# print(j)

# d={"a":1,"b":3}
# x=d["a"]
# print(x)
# v=d.values()
# k=d.keys()
# print(v)
# print(k)
# g=d.get("a")
# print(g)


# import random
# import numpy as np
# r=np.random.randint((1,6),3)
# print(r)

# import random
# #Generate 5 random numbers between 10 and 30
# randomlist = random.sample(range(10, 30), 5)
# print(randomlist)

# """""""""""""""""""""""""Permutaion""""""""""""""""""""
# l=[3,2,1]
# for i in range(0,len(l)):
#     for j in range(0,len(l)):
#             l[i],l[j]=l[j],l[i] 
#             print(l)

# """""""Increase tuple""""       
# t1=(1,2,3)
# t2=(4,5,6) 
# t1=t1+t2
# print(t)

# s1="abc de f   "
# s2="bca"
# if sorted(s1)==sorted(s2):
#     print("It is anagram")

# print(list(s1))
# print(s1.split("-"))
# print(".".join(s1),end=" ")
# print(s1.replace(" ",""))


# import re
# s1="abc de f   "
# w=r"\s+"
# after=re.sub(w,"",s1)
# print(after)


# s1="abc de f   "
# s=[]
# for i in range(0, len(s1)):
#     if not s1[i]==" ":
#         # print(s1[i])
#         s.append(s1[i]) 
# print(''.join(s),end="") 


# s1="abc de ff   "
# d={k:s1.count(k) for k in s1.split() }
# print(d)

# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# res = []
# [res.append(x) for x in test_list if x not in res]
# print(res)

# l=[1,2,33,4,55,3,3,6,7,8,55,5,9,9,2]
# x=list(map(lambda a:a*a,l))
# print(x)
# y=list(filter(lambda a:a>10,l))
# print(y)
# z=reduce(lambda a,b:a+b,l)
# print(z)

# """"""""""remove duplicate"""
# l=[1,2,33,4,55,3,3,6,7,8,55,5,9,9,2]
# k=[]
# for i in l:
#     if i not in k:
#           k.append(i)
# print(k)

# l=[24,3,48,5,22,11]
# m=l[0]
# for i in range(0,len(l)):
#     if l[i]>m:
#        m=l[i] 
# print(m)

# print(list(i for i in range(0,11)))

# str="abcdefg"
# x=str[-3:-6:-1]
# print(x)

# import validators
# valid=validators.url('https://www.codespeedy.com/')
# if valid==True:
#     print("Url is valid")
# else:

#     print("Invalid url")

# Number = 123   
# Reverse = 0    
# while(Number > 0):    
#     Reminder = Number %10   
#     Reverse = (Reverse *10) + Reminder    
#     Number = Number //10    
# print("\n Reverse of entered number is = %d" %Reverse)
# print("Reverse of entered number is =",Reverse )

# n=123
# rev=0
# while n>0:
#     rem=n%10
#     # print(rem)
#     rev=(rev*10)+rem
#     print(rev)
#     n=n//10
#     # print(n)
# # print(rev)   

# def deco(abc):
#     def inner():
#         abc()
#         print("Devendra")
#     return inner
# @deco
# def abc():
#     print("Hello")
# abc()    


# import json
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# # parse x:
# y = json.loads(x)
# # the result is a Python dictionary:
# print(type(y),y["age"])
# print(y)

# import json
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# # convert into JSON:
# y = json.dumps(x)
# # the result is a JSON string:
# print(type(y),y)

# print(ord("c"))
# print(chr(99))

# import sys
# t=(1,2,3,4)
# l=[1,2,3,4]
# print(sys.getsizeof(t), sys.getsizeof(l))

# l=["a","b","c","ddetr"]
# print(l[-1][-1])

# st="The kapil sharma show"
# k=[]
# str1=" "
# for i in st.split():   
#     k.append(i[::-1])
# m=str1.join(k)
# print(m,type(m))

# rows = int(input("Enter number of rows: "))
# number = 1
# for i in range(1, rows+1):
#     for j in range(1, i+1):
#         print(number, end=" ")
#         number += 1
#     print()

# s="devendraaaaa"
# d={i:s.count(i) for i in s}
# K= max(d, key= lambda x: d[x])
# K2= min(d, key= lambda x: d[x])
# print(K,d.get("a"))
# # print(d.keys())

# dd={"a":4,"b":5,"c":7}
# print(list(dd.keys()))
# print(list(dd.values()))
# i=max(dd)
# print(i,dd.get(i))

# string="Devendra123"
# for a in string:
#     if (a.isnumeric()) == True:
#         print(a)

# import re 
# s="de-vend_ra"
# k=re.search("-(.*)_",s)
# print(k.group(1))


# a="devendra"
# s=[]
# for i in a:
#     s.append(i)
# k="".join(s)
# print(k,type(k))


# check_float = isinstance(25.9, float)
# print(check_float)

# check_int= isinstance(25.9, int)
# print(check_int)


# d={1:2,3:4,5:{11:12},7:8}
# print(d[4][11])

# print(l1)
# print(l2)
# k=[]
# for i in l2:
#     k.extend(list(i))
# print(k)


# d={1:2,3:4,5:{11:12},7:8}
# for i in d.keys():
#     k=d.get(i)
#     print(k)
#     for j in k:
#         if j in k.get(j): 
#             print("It is present")

# k=d[i][j]
# if k==12:
#     print(d[i][j])


# d={1:2,3:4,5:{11:12},7:8}
# l1=list(d.keys())
# l2=list(d.values())
# k=[]
# for i in l2:
#         if isinstance(i,int):
#                 k.append(i)
#         if isinstance(i,dict):
#                 l=k.append(list(i.values())[0])     
# print(k)
# if 12 in k:
#         print("It is present")


# d={1:2,3:4,5:{6:12},7:8}
# if 12 in list(d.items()):               
#         print("T")
# else:
#         print("N")

# def even_numbers(n):
#         x=1
#         y=1
#         z=0
#         for x in range(n):
#                 x=y
#                 y=z
#                 z=x+y
#                 yield z       
# num = even_numbers(10)      
# print(list(num))

# def even_numbers(n):
#         for x in range(n):
#                 yield x       
# num = even_numbers(10)      
# print(list(num))

# d={1:"a",2:"b",3:"c"}
# val="c"
# print(d.items())
# for key, value in d.items():
#         if val==value:
#                 print(key)

# def deco(add):
#     def inner():
#         a=add()
#         b=a+4
#         print(b)
#     return inner   
# @deco
# def add():
#     a=56
#     return a
# add()

# class A:
#         ad=40
#         def add(slef):
#            a=4+8
#            print(a)     
# class B(A):
#         super().
#         def add(slef):
#            a=4+4
#            print(a) 
#         def sub(self):
#                 super().add
#                 # self.ad=30
#                 a=self.ad-10
#                 print(a)

# obj=B()
# obj.add()
# obj.sub()


# def my_function(x):
#   return list(dict.fromkeys(x))
# mylist = my_function(["a", "b", "a", "c", "c"])
# print(mylist)

# x=["a", "b", "a", "c", "c"]
# y=list(dict.fromkeys(x))
# print(y)

# k=int(input("Enter any number to check weather it is duplicate or not "))
# l1=[1,2,2,3,3]
# if l1.count(k)>=2:
#         print("Count= ",l1.count(k))
# else:  
#         print("No duplicate number found.")

# l1=[1,2,3]
# l2=[4,5,6]
# d1={3:"a",1:"b",2:"c"}
# d2={4:"d",5:"e",6:"f"}
# d3={4:"u"}
# # print(d1|d2)
# # d1.update(d3)

# print(sorted(d1.values()))# print(l1|l2)
# dt={key:value for key,value in sorted(d1.items())}
# print(dt)
# print(dict(sorted(d1.items())))

# d1.pop(1)
# del d1[1]
# print(d1)

# class Vehicle:
#         def abc(self,name):
#                 print("Hellow Dev")
# v=Vehicle()
# print(type(v).__name__)

# class A:
#     i=30
#     j=40
#     def xyz(self):
#         self.a=10
#         self.b=20
#         print("Hello A.xyz")
#     def abc(self):
#         print('Hello A.abc')
#         sum=self.i+self.j
#         print(sum)

# class B(A):
#     def abc(self):
#         super().xyz()
#         super().abc()
#         c=self.a+self.b
#         k=self.i+self.j   
#         print(c,k) 
# obj=B()
# obj.abc()

# def deco(add):
#     def inner():
#         a=add()
#         b=a+4
#         print(b)
#     return inner   
# # @deco
# def add():
#     a=56
#     return a
# add()

# def lst():
#         for i in range(10):
#                 yield i
# print(list(lst()))
# # print(next(k))
# # print(next(k))
# # print(next(k))
# # print(next(k))


# class St_method:
#         @staticmethod
#         def add():
#                 print("Hello Dev")
# St_method.add()

# from datetime import date
# from datetime import datetime  
# class Test: 
#     def beg():  
#         # print ("Welcome to the World!!")     
#         print(date.today())
#         print(datetime.now().time())
# Test.beg()

# Return the current date and time of the system   
# Current_time = datetime.now().time()   
# print("Current time is :", Current_time)

#########two list into dictinary ##############
# l1=["a","b","c","d"]
# l2=[3,4,1,2]
# print(l1+l2)
# d=dict(zip(l1,l2))
# print(d)
# 
# l3=[]
# l4=[]
# for key,value in d.items():
#         l3.append(key)
#         l4.append(value)
# 
# print(l3)
# print(l4)

# d2={'b': 1, 'c': 2, 'a': 3}
# d={key:value for value,key in d2.items()}
# print(d)
# dl={key:value for key,value in sorted(d2.items())}
# print(dl)

# def perm(start, end=[]):
#     if(len(start) == 0):
#         print(end)
#     else:
#         for i in range(len(start)):
#             perm(start[:i] + start[i+1:], end + start[i:i+1])
# perm([1,2,3])

""""Inbuilt function"""

# d=abs(-12)
# d=chr(98)
# d=ord("d")
# d=pow(2,3)
# d=round(23.4)
# d=divmod(5,3)
# print(d)


# """""""""""""""""""""""""Sorting""""""""""""""""""""
# l=[3,1,2,4,5,7,89,43]
# def sort(l):
#     for i in range(len(l)):
#         for j in range(i):
#             if l[j]>l[i]:
#                 l[i],l[j]=l[j],l[i]
#     print(l)
# sort(l)
#
# l=[888,2,3,7,45,22,9]
# def max_value(l):
#     m = l[0]
#     for i in range(1,len(l)):
#         if l[i]>m:
#             m=l[i]
#     print(m)
# max_value(l)

# j=int(input("Any element to find in dictionary "))
# d={1:2,3:4,5:{11:12},7:8}
# l=list(d.values())
# print(list(d.keys()),list(d.keys()))
# k=[]
# for i in l:
#         if isinstance(i,int):
#                 k.append(i)
#         if isinstance(i,dict):
#                 l=k.append(list(i.values())[0])
# if j in k:
#         print("It is present")
# else:
#         print("It is not present")


# def return_sum(l):
#     even_sum = 0
#     odd_sum = 0
#     for i in l:
#         if i % 2 == 0:
#             even_sum = even_sum + i
#         elif i % 2 != 0:
#             odd_sum = odd_sum + i
#     return [even_sum, odd_sum]
# l = [23, 33, 45, 78, 56, 12, 46, 39, 80]
# print(return_sum(l))

# from functools import reduce
#
l = [3, 4, 5, 6, 1, 2]
# x = list(map(lambda a: a * 2, l))
# print(x)
#
# y = list(filter(lambda a: a > 2, l))
# print(y)
#
# z = reduce(lambda a, b: a + b, l)
# print(z)
#
# list_comp = [item * 2 for item in l]
# print(list_comp)
#
# list_comp1 = [item * 2 for item in l]
# print(list_comp)
#
dt = {"e": 3, "b": 5, "c": 9, "d": 6}
x=sorted(dt.values())
print(x)
# d = {value: value ** 2 for value in l}
# print(d)
d = {key: value for key, value in sorted(dt.items())}
print(d)
print(d["e"])

