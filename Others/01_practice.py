# import sys
# print(sys.version)
# print(sys.version_info)

# import datetime
# now=datetime.datetime.now()
# print (now.strftime("%c"))

# from math import pi
# r=float(input("Enter The value of radius: "))
# a=pi*r*r
# print("Area of circle is = ",a)

# f_name=input("Enter the fisrt name: ")
# l_name=input("Enter the last name: ")
# print("Your name is: ", l_name,f_name)

# number=input("Enter numbers with comma : ")
# c=list(number)
# print(c)
# a=number.split(",")
# b=tuple(a)
# print(a)
# print(b)

# f_name=input("Enter the file name: ")
# ext_file=f_name.split(".")
# a=ext_file[-1]
# b=repr(ext_file[-1])
# print(a)
# print(b)


# color_list = ["Red","Green","White" ,"Black"]
# print("First and last color is: "+color_list[0],color_list[-1])

# exam_st_date = (1111, 12, 21)
# print("The examination will start from : %i / %i / %i" % exam_st_date)
    
# import calendar
# print(calendar.month(2021,5))


# from datetime import date
# f_date=date(1986,1,21)
# l_date=date(2021,5,5)
# days_t=l_date-f_date
# print(days_t.days)

# num=int(input("Enter any number: "))
# if num<200 and num>100:
#     print("Your entered number is between 100 to 200")
# else:
#     print("number is out of between 100 to 200")

# def strt(str,n):
#     result=""
#     for i in range(n):
#         result=result+str
#     return result
# print(strt(".py",3))

# num=int(input("Enter any number: "))
# if num%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")   

# list1=[2,3,4,5,6,4,7,4]
# print(list1.count(4))

# def list1(lst):
#     r=lst.count(4)
#     return r
# print(list1([1,2,3,4,5,4,4]))

# def lst(item):
#     for i in item:
#         j=""
#         while i>0:
#             j+="*"
#             i=i-1
#         print(j)
# lst([8,4,3,6])


# str=input("Enter any letter: ")
# # lst=["a","e","i","o","u"]
# lst="aeiou"
# if str in lst:
#    print("Vowel")
# else:
#    print("consonent")     

# def lcm(x,y):
#         if x>y:
#             z=x
#         else:
#             z=y
#         while True:
#             if z%x==0 and z%y==0:
#                 lcm=z
#                 break
#             z+=1
#         return lcm
# print(lcm(6,4))

# def sum(x,y,z):
#     if x==0 or y==0 or z==0:
#         z=0
#         return z
#     else:
#         z=x+y+x
#         return z
# s=sum(1,2,1)
# print(s)

# def sum(x,y):
#     z=x+y
#     if z>15 and z<20:
#         z=20
#         return z
#     else:
#         z=x+y
#         return z
# s=sum(10,6)
# print(s)

# def sum(x,y):
#     z=x+y
#     if x==y or z==5 or x-y==5 or y-x==5:
#         return True
#     else:
#         return False
# s=sum(5,10)
# print(s)

# def add_numbers(a, b):
#     if not ((a, int) and (b, int)):
#          raise TypeError("Inputs must be integers")
#     return a + b

# print(add_numbers(10, 10))

# def employee(name, age, address):
    
#     print(f"My name is {name}\nMy age is {age}\nI am from {address} ")

# employee("Devendra",35,"Orai")

# import math
# p1 = [4, 0]
# p2 = [0, 0]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
# print(distance)

# For 32 bit it will return 32 and for 64 bit it will return 64
# import struct
# print(struct.calcsize("P") * 8)

# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())

# import site; 
# print(site.getsitepackages())

# from subprocess import call
# call(["ls", "-l"])

# import multiprocessing
# print(multiprocessing.cpu_count())

# import os
# print("Current File Name : ",os.path.realpath(__file__))

# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
# print(files_list)

# import platform
# import os
# import struct
# print(platform.system())
# print(platform.release())
# # print(struct.calcsize("P"*8))

# import site; 
# print(site.getsitepackages())

# import os
# print("Current File Name : ",os.path.realpath(__file__))

# def my_function(*kids):
#   print("The youngest child is " + kids[2])


# n=[2,4,6,8]
# res=1
# for x in n[1:3]:
#   res*=x
# print(res)
# print(n[1])

# import math
# p1=[4,1]
# p2=[5,2]
# d=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
# print(d)

# from __future__ import print_function
# import sys
# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)

# eprint("abc", "efg", "xyz", sep="--")

# import getpass
# print(getpass.getuser())

# import time
# import datetime

# def sum_of_n_numbers(n):
#     start_time = time.time()
#     s = 0
#     for i in range(1,n+1):
#         s = s + i
#     end_time = time.time()
#     return s,end_time-start_time
# n = 5
# print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))


# import glob
# import os
# files = glob.glob("*.txt")
# files.sort(key=os.path.getmtime)
# print("\n".join(files)

# import math
# math_ls=dir(math)
# # print(math_ls)
# print(dir(math))

# import sys
# print("\nPython Copyright Information")
# print(sys.copyright)
# print()

# import sys
# print("This is the name/path of the script:"),sys.argv[0]
# print("Number of arguments:",len(sys.argv))
# print("Argument List:",str(sys.argv))

# import sys
# str1="Devendra Singh Shakya"
# print(sys.getsizeof(str1), "Bytes")

# import sys
# print()
# print("Current value of the recursion limit:")
# print(sys.getrecursionlimit())
# print()

# list_of_colors = ['Red', 'White', 'Black']  
# colors = '-'.join(list_of_colors)
# print()
# print("All Colors: "+colors)
# print()

# l=[10,20,30]
# s = sum(l)
# print("\nSum of the container: ", s)
# print(type(s))

# s = "The quick brown fox jumps over the lazy dog."
# print()
# print(s.count("d"))
# print()

# import os
# path="kivy"
# if os.path.isdir(path):
#     print("It is Driectory")
# elif os.path.isfile(path):
#     print("It is file")
# else:
#     print("it is special file")

# print(ord("A"))
# print(ord("a"))
# print(ord("@"))
# print(ord("Z"))

# import os
# file_size = os.path.getsize("2.txt")
# print("\nThe size of abc.txt is :",file_size,"Bytes")

# a=20
# b=30
# print("Before swap:", a,b)
# # a,b=b,a
# ====or====
# t = a
# a = b
# b = t
# print("After swap:", a,b)

# import time
# print(time.ctime())

# import os
# os.system("cls")

# import platform
# host_name = platform.uname()
# print("Host name:", host_name )


# import requests
# data = requests.get('https://www.mojambik.com/')
# print(data.text)

# import json
# print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))

# =====Decimal to hexadecimal========
# x = 15
# print(format(x, '02x'))
# x = 4
# print(format(x, '02x'))

# import platform
# hostname=platform.uname()
# print(hostname)

# import struct
# print(struct.calcsize("P") * 8)

# def max_of_three( x, y, z ):
#     if x > y and y > z:
#         print(x)
#     elif z>y:
#         print(z)
#     else:
#         print(y)
# max_of_three(12,34,55)

# nl=[]
# for x in range(1500,2700):
#     if(x%7==0 and x%5==0):
#         nl.append(str(x))
# print(",".join(nl))

# for x in range(1,6,1):
#     print("*"*x)
#     x=x+1
# for n in range(4,1,-1):
#     print("*"*n)
    
# =========Reverse string=========
# w = "devendra"
# for x in range(len(w) -1, -1, -1):
#   print(w[x], end="")
  



