# This commnent
# import cv2
# import math
# # print("Hello World")
# # print(7+7)
# # print(math.gcd(3,6))
# a=34
# # b="Devendra"
# # c=45.32
# d=2
# # print(a+c)
# # print(c/d)
# # typeA=type(a)
# # typeB=type(b)
# # typeC=type(c)
# # print(typeC)
# # print(a+c)
# # e="31"
# # e=int(e)
# # print(e+2)
# # e=type(e)
# # print(e)
# name="  Devendra, Manan, Ketan  "
# # print(name)
# # print(name[2:6])
# # print(name.strip())
# # print(len(name))
# # var=name.lower()
# # var=name.upper()
# # print(var)
# # var=name.replace("e", "a")
# # var=name.replace(",","\n")
# # # print(var)
# # stri1="This is a"
# # stri2="This not ok"
# # print(stri1+stri2)
# # print(stri1+name)
# # name1="Manan"
# # name2="Ketan"
# # temp="This is a {1} and he is good boy named {0}.". format(name1, name2)
# # temp=f"This is a {name2} and he is good boy named {name1}"
# # print(temp)
# # k=2**3 # **Exponential operator
# # print(k)
# # k=4//2 # //Floor Operator
# # print(k)
# # k=7%3 # % Module Operator
# # print(k)
# '''
# Python Collection
# 1-list
# 2-Tuple
# 3-set
# 4-Dictionary
# '''
# # List
# # lst=[21,42,55,7,23,1]
# # print(lst)
# # var=type(lst)
# # print(var)
# # var=lst[2]
# # lst[3]=77
# # var=lst[3]
# # print(var)
# # print(lst)
# # var=type(lst)
# # var=len(lst)
# # print(var)
# # lst.append(100)
# # lst.insert(1,100)
# # lst.remove(42)
# # lst.pop()
# # del lst[2]
# # del lst
# # lst.clear()
# # var=lst
# # print(var)

# # Tuple
# # a=("Ketan", "Manan", "Dev")
# # var=type(a)
# # print(var)

# # Set
# s1={12,2,4,5,3,5,3,2,5,6,8,5,4,2,1}
# # s1.add(342)
# # s1.update([23,44,55,66])
# # print(len(s1))
# # s1.discard(12)
# # We can use also .pop, .pop, .clear, intersection, .union
# # print(s1)
# # Dictionary
# # devDict={
# #     "Name":"Manan",
# #     "Class":"1st",
# #     "Marks":90
# #}
# # devDict["Marks"]=69
# # We can use .pop, .del, .clear, .update
# # print(devDict["Marks"])
# # print(devDict)
# age=34
# age=input("Enter Your Age\n")
# age=int(age)
# if(age>18):
#         print("You can drive")
# elif(age==18):
#         print("You are awsome teen")
# else:
#     print("You cant drive")

# loops
# for i in range(0, 10000):
#  print(i+1)

# li=[12,11,"Manan"]
# for items in li:
#     print(items)

# tpl=(2,4,"Ketan")
# for tuple in tpl:
#  print(tuple)

# s1={2,3,4,5,3,2,1,2,12,15}
# for set in s1:
#     print(set)

# dikt={
#     "Name":"Manan",
#     "Age":"6 Years",
#     "Marks":69
# }
# for dictionary in dikt:
#  print(dictionary)

# i=0
# while(i<100):
#  i=i+1
# #  if i==78:
# #     #  break
# #     continue
# #  print(i+1)

# # def greet():
# #    print("Good Morning sir")
# #    print("Good Morning Uncle")
# #    print("Good Morning Madam")
# # greet()

# # def sum(a,b):
# #    print("Value of d")
# #    c=a+b
# #    return(c)
# # d=sum(3,5)
# # print(d)

# # def get_formatted_name(first_name, last_name):
# #  """Return a full name, neatly formatted."""
# #  full_name = first_name + ' ' + last_name
# #  return full_name.title()
# # musician = get_formatted_name('jimi', 'hendrix')
# # print(musician)
# import sys
# import pygame
# def run_game():
# Initialize game and create a screen object.
#  pygame.init()
#  screen = pygame.display.set_mode((1200, 800))
#  pygame.display.set_caption("Alien Invasion")
# # Start the main loop for the game.
#  while True:
# # Watch for keyboard and mouse events.
#   for event in pygame.event.get():
#    if event.type == pygame.QUIT:
#     sys.exit()
# # Make the most recently drawn screen visible.
#   pygame.display.flip()
# run_game()
# # from turtle import *
# # from random import randrange
# # from freegames import square, vector

# # food = vector(0, 0)
# # snake = [vector(10, 0)]
# # aim = vector(0, -10)

# # def change(x, y):
# #     "Change snake direction."
# #     aim.x = x
# #     aim.y = y

# # def inside(head):
# #     "Return True if head inside boundaries."
# #     return -200 < head.x < 190 and -200 < head.y < 190

# # def move():
# #     "Move snake forward one segment."
# #     head = snake[-1].copy()
# #     head.move(aim)

# #     if not inside(head) or head in snake:
# #         square(head.x, head.y, 9, 'red')
# #         update()
# #         return

# #     snake.append(head)


# #     if head == food:
# #         print('Snake:', len(snake))
# #         food.x = randrange(-15, 15) * 10
# #         food.y = randrange(-15, 15) * 10
# #     else:
# #         snake.pop(0)

# #     clear()

# #     for body in snake:
# #         square(body.x, body.y, 9, 'black')

# #     square(food.x, food.y, 9, 'green')
# #     update()
# #     ontimer(move, 100)

# # setup(420, 420, 370, 0)
# # hideturtle()
# # tracer(False)
# # listen()
# # onkey(lambda: change(10, 0), 'Right')
# # onkey(lambda: change(-10, 0), 'Left')
# # onkey(lambda: change(0, 10), 'Up')
# # onkey(lambda: change(0, -10), 'Down')
# # move()
# # done()

# # thisset={23,21,33,33,11,6,55,55,44}
# # # typeA=type(thisset)
# # # print(typeA)
# # print(len(thisset))
# # a=input("Enter the value of a=")
# # b=input("Enter the value of b=")
# # if b>a:
# #   print("b is greater then a")
# # elif a==b:
# #   print("a and b are equal")
# # else:
# #   print("a is greater then b")  

# # i=1
# # while i<6:
# #  print(i)
# #  if i==3:
# #   break
# #  i+=1 

# # i=0
# # while i<6:
# #  i+=1 
# #  if(i==3):
# #    continue
# #  print(i)

# # fruits=["Apple", "Mango", "Orange"]
# # for x in fruits: 
# #  if x=="Orange":
# #   break
# #  print(x)

# # fruits=["Apple", "Mango", "Orange"]
# # for x in fruits: 
# #  if x=="Mango":
# #   continue
# #  print(x)

# # for x in range(6):
# #  print(x)range

# # else:
# #   print("Finished")

# # for x in range(30,2, -2):
# #  print(x)
# # else:
# #   print("Finished")
# # number=[1,2,3,]
# # adj=["Red","Green", "Yellow"]
# # fruits=["Apple", "Mango", "Orange"]
# # for x in adj:
# #   for y in fruits:
# #     for z in number: 
# #      print(z,x,y,)

# # def my_function():
# #   print("Hello my_function")
# # my_function()

# # def my_function():
# #   print(3+4)
# # my_function()

# # def my_function(fname):
# #   print(fname + " refrence")
# # my_function("email")
# # my_function("Mobile")
# # my_function("Addrs")

# # def my_function(fname="India"):
# #   print(" I am from " + fname)
# # my_function("England")
# # my_function("Norway")
# # my_function("Japan")
# # my_function()

# # def my_function(x):
# #   return x*5
# # print(my_function(10))
# # print(my_function(20))
# # print(my_function(30))

# # car=["Toyota", "BMW", "Suzuki"]
# # # car.insert(2, "Tata")
# # car.sort()
# # print(car)

# # class Myclass:
# #  x=5
# # p1=Myclass()
# # print(p1.x)

# # class Person:
# #  def init(self, name, age):
# #   self.name=name
# #   self.age=age
# # p1=Person("John", 36)
# # print(p1.name)
# # print(p1.age)

# # def function_farnt():
# #  celcius=float(input("enter the value of celcius="))
# #  fahrenheit=(celcius*9)/5+32
# #  print("Value in Fahrenheit=", fahrenheit)

# # function_farnt()

# # x=abs(3+5j)
# # print(x)

# # mylist=[True, True, True]
# # x=all(mylist)
# # print(x)

# # x=format(0.5, "%")
# # print(x)

# # class person:
# #   name="Manan"
# #   age="7 Years"
# #   country="India"
# # x=getattr(person, "name", "age")
# # print(x)

# # x=('apple', 'mango', 'banana')
# # y=id(x)
# # print(y)

# # def myfunc(n):
# #  return len(n)
# # x=map(myfunc,('apple', 'mango', 'banana'))
# # myfunc(n)

# # x=min(4,10)
# # print(x)

# # x=pow(3,4)
# # print(x)

# # class person1:
# #  name="Manan"
# #  age=37
# #  country="India"
# # x=setattr(person1, 'age', 10)
# # print(x)

# # x=('aaple', 'mango', 'banana')
# # y=enumerate(x)
# # list(y)
# # print(y)

# # mylist=[1,2,9,11,3,4,5,6,7]
# # # lst=mylist.copy()
# # # lst.clear()
# # # print(lst)
# # # lst=mylist.pop(3)
# # mylist[3]=13
# # # lst=len(mylist)
# # print(mylist)

# # tuple1=(1,2,3,4,5,6,7)
# # tpl=tuple1.index(5)
# # print(tpl)

# # mystr="My name is Devendra"
# # # str=mystr.upper()
# # print(len(mystr))

# # myset={1,2,3,4,4,3,2,4,4,4,3,3}
# # myset.update([3,4,4,4,8,7])
# # myset.discard(7)
# # print(myset)

# # my_dict={    
# #     "customer name": "Ruby Patel",
# #     "Orader ID":1234,
# #     "Segment":"Machine"
# # }
# # # print(my_dict)
# # dkt=my_dict["customer name"]="Manan"
# # # my_dict["Region"]="west"    
# # # print(my_dict) 


# from tkinter import *
# class Window(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.pack(fill=BOTH, expand=1)
        
#         text = Label(self, text="Just do it", )
#         text.place(x=70,y=90)
#         # text.pack()
        
# root = Tk()
# app = Window(root)
# root.wm_title("Tkinter window")
# root.geometry("500x200")
# root.mainloop()

# # from tkinter import*
# # window=Tk()
# # window.geometry('500x300') 
# # window.title("GUI") 
# # w=Label(window, text="Hello GUI !")
# # bt=Button(window, text="Enter")
# # bt.grid(column=1, row=0)
# # w.pack()
# # window.mainloop()

# # from tkinter import *
# # root=Tk()   
# # root.geometry("350x200")
# # root.minsize(200,100)
# # root.maxsize(600,600)
# # manan=Label(text="Manan is a good boy.")
# # manan.pack()
# # root.mainloop()

# from tkinter import *
# # from tkinter import ttk
# from PIL import Image, ImageTk
# root=Tk()   
# root.geometry("350x200")
# lbl=Label(text="Nature is Almighty")
# lbl.pack()
# image = Image.open("wall.jpg")
# pic = ImageTk.PhotoImage(image)
# # pic=ImageTk.PhotoImage(image=Image.open("C:/NF/wall.jpg"))
# Nature=Label(image=pic)
# Nature.pack()
# root.mainloop()

# from tkinter import *
# root=Tk()
# root.geometry("400x333")
# root.title("This is Devendra Shakya...")
# lbl=Label(text='''The eldest son of screenwriter Salim Khan.. 
# \n The eldest son of screenwriter Salim Khan..
# \n The eldest son of screenwriter Salim Khan''', bg="red", fg="white", padx=22, pady=33, font="arial 15 italic", borderwidth=3,relief=RIDGE)
# lbl.pack(side="right", fill=Y, padx=33, pady=44)
# root.mainloop()
 

# from tkinter import*
# root=Tk()
# root.geometry("600x300")
# root.title("Hidusatan News")
# lbl=Label(text='''राम गोपाल वर्मा की फिल्म 'मर्डर' पर फाइल हुआ केस, फिल्ममेकर ने कहा- 
# \n किसी को नीचा दिखाने का मेरा कोई इरादा नहीं था''', bg="red")
# lbl.pack(anchor="nw", side=LEFT, padx=12, pady=12)

# lbl=Label(text='''बालास्वामी, विक्टिम प्रणय के पिता ने राम गोपाल वर्मा की इस फिल्म के खिलाफ कोर्ट में अर्जी दाखिल की है। 
# \n उनका कहना है कि कोर्ट में केस अभी तक पेंडिंग है,''', bg="yellow")
# lbl.pack(anchor="nw", side=RIGHT, padx=12, pady=12)


# lbl=Label(text='''इसपर राम गोपाल वर्मा ने ट्वीट करते हुए सफाई पेश की है। राम गोपाल वर्मा लिखते हैं 
# \n कि मर्डर पर होने वाले केस पर मैं बता दूं कि मेरी यह फिल्म पूरे तरीके से सच्ची घटना पर आधारित है ''', bg="orange")
# lbl.pack(anchor="nw", side=RIGHT, padx=12, pady=12)


# root.mainloop()


# from tkinter import*
# root=Tk()
# root.geometry("400x200")
# f1=Frame(root,bg="yellow", borderwidth=6, relief=GROOVE)
# f1.pack(side=LEFT,fill=Y)
# f2=Frame(root,bg="blue", borderwidth=6, relief=GROOVE)
# f2.pack(side=TOP,fill=X)

# lbl=Label(f1, text="Frame example", font="Arial 16 bold", pady=190)
# lbl.pack()  
# lbl=Label(f2, text="Welcome to Python", font="Arial 16 bold",fg="red", padx=190)
# lbl.pack()  

# root.mainloop()

# from tkinter import*
# root=Tk()
# root.geometry("350x250")
# def hello():
#  c=4+9
#  print(c)
# def name():
#     name=input("Enter the name>>>")
#     print(name)

# f1=Frame(root, bg="red", relief=GROOVE)
# f1.pack(side=LEFT, anchor="nw")
# bt=Button(f1, bg="green", text="Print", font="Arial 9 bold", command=hello)
# bt.pack(side=LEFT, padx=10)
# bt1=Button(f1, bg="yellow", text="Your name", font="Arial 9 bold",command=name)
# bt1.pack(side=RIGHT, padx=10)
# root.mainloop()

# from tkinter import*
# root=Tk()
# root.geometry("400x300")
# root.title("Example")
# def getval():
#     print("Value of username is>>>", uservalue.get())
#     print("Value of Password is>>>", passvalue.get())    
# user=Label(root, text="Username", relief=GROOVE)
# pwd=Label(root, text="Password", relief=GROOVE)
# user.grid(column=0, row=0)
# pwd.grid(column=0, row=1)
# uservalue=StringVar()   
# passvalue=StringVar()
# userentry=Entry(root, textvariable=uservalue)
# passentry=Entry(root, textvariable=passvalue)
# userentry.grid(column=1, row=0)
# passentry.grid(column=1, row=1)
# bt=Button(root, text="submit", command=getval)
# bt.grid(column=0, row=2)  
# root.mainloop()


# print("Please enter Two Numbers\n")
# print("Please enter first number=")
# first_num=input()
# print("Please enter Second number=")
# sec_num=input()
# print("Sum of your numbers is =", int(first_num)+int(sec_num))

# str1="My name is Manan"
# print(str1[4: :])

# d2={"Manan":"Mango", "Ketan":"Banana", "Ranjana":"Apple"}
# d2["Dev"]="Grapes"
# del d2["Manan"]

# d3=d2.copy()
# print(d3)

# var1=6
# var2=45
# list1=[5,8,9]
# var3=int( input("Enter a number  "))
# if var3 in list1:
#     print("Yes")
# elif var3==var1:
#     print("Equal")
# else:
#     print("No")  



# dict1={"Manan":"13/01/13",
# "Ketan":"12/02/14",
# "Dev":"21/01/86"}
# var1=input("Enter the name of student  ")
# if var1 in dict1:
#     print(dict1[var1])

# list1=["Manan", "Ketan", "Dhruv", "Dev",2,10, 6,7,8,9]
# for item in list1:
#      if str(item).isnumeric():
#         print(item)      

# i=1
# while(i<=9):
#     if i==5:
#         continue
#     print(i, end="")
#     i=i+1
#     if i==7:
#         break 

# list1=[["Manan",1], ["Ketan",3], ["Dhruv",4], ["Dev",5]]
# dict1=dict(list1)
# for item, lolypop in dict1.items():
#  print(item,"is has", lolypop)

# dict1={"Devendra":123, "Manan":456, "Ketan":789}

# for item, item1 in dict1.items():
#     print(item, item1)

# i=int(input("Enter a Number  "))
# while(True):
#     if i<=5:
#         i=i+1
#         continue
#     print(i, end=" ")
#     i=i+1
#     if (i>44):
#      break

# tup1=("dev", "kishan", "raju")
# print(type(tup1))  
# for item1 in tup1:
#     print(item1)


# a=int(input("Enter value A   "))
# b=int(input("Enter value of B    "))
# print("A bada hai B se ")if a>b else print("B bada hai A se") 

# def function1():
#     """This function is for Sum"""
#     a=int(input("Enter the value of A="))
#     b=int(input("Enter the value of B="))
#     sum=a+b   
#     print(sum)
#     return sum
# print(function1.__doc__)

# from tkinter import *
# root=Tk()
# root.geometry("120x120")
# bt=Button(text="devendra")
# bt.pack()
# root.mainloop()


# a=input("Enter the value of A=")
# b=input("Enter the value of B=")
# try:
#     print("Sum of these numbers is=", int(a)+int(b))
# except Exception as e:
#     print (e)
# print("This line is very important")

# f=open("davshakya.txt", "r")
# content=f.read()
# print(content)
# # for line in f:
#    print(line, end=" ")
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()


# """Guess the number"""
# n=10
# x=9
# a=int(input("Enter Guess Number..."))
# while True:
#     x=x-1
#     if a>n and x!=10:
#         print("Enter lesser number...")
#         a=int(input())
#     elif a<n and x!=0:
#         print("Enter greater number...")
#         a=int(input())
#     elif a==n:
#         print("Congrats! Correct again") 
#         print("Attempt left =", x)
#         print("Attempt used=, 9-x)
#         break
#     else:
#         print("Gamve Over! out of attempts", )
#         break   


# f=open("davshakya.txt", "r")
# content=f.read()
# print(content)
# f.close()


# f=open("davshakya.txt", "a")
# a=f.write("devendra bahut acche hai\n")
# f=open("davshakya.txt", "r")
# print(a)
# content=f.read()
# print(content)
# f.close()

# f=open("textfile.text", "w")
# f.write("\nHello Devendra\nKaise hai bhai")
# f=open("textfile.text", "r")
# content=f.read()
# print(content)
# f.close

# f=open("textfile.text","a+")
# f.write("Thank you")
# print(f.read())

# n=5
# a=int(input("Enter the number for printing star="))
# while true:
#     n=n-1
#     if a<n:
#         print("*")
#         a=a+1
#         break
#     elif a>n:
#         print("*")
#         a=a-1
#         break
#     else:
#         print("Wrong Number")
#         break

# a=int(input("Enter any number"))
# for a in range (2, 6):
#     for i in range (1,a):
#             print("*", end="")
        
#     print()

# k=int(input("Enter the of max number of star ="))
# for a in range (2,k+2,1):
#     for i in range (1,a):
#         print("*", end="")
#     print()        
    
# k=int(input("Enter the of max number of star ="))
# for a in range(1, 6):

# k=10
# for a in range(1,k):
#     a=a+k
#     for i in range (1,a):
#         print("*", end="")
#     k=k-2
#     if k==-8:
#         break
#     print()

# for a in range(5,1,-1):
#     for i in range (1,a):
#         print("*", end="")
#     print()     

# f=open("davshakya.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.seek(0)
# print(f.readline())
# f.close()

# f=open("davshakya.txt")
# print(f.readlines())
# f.close()

# with open("davshakya.txt") as f:
#     a=f.read(4)
#     print(a)    
# f=open("davshakya.txt", "r")    
# print(f.readline())

# x=9
# def function1(n):
#     print(n, "I am hero")
# function1("He is hero and ")


# x=9
# def function1():
#     k=3
#     global x
#     x=7
#     c=x+k
#     print(c)
# function1()

# def function1():
#     x=8
#     def function2():
#         global x
#         x=77
#         print(x)  
#     function2() 
#     print(x)
# function1()

# add=lambda x,y:x+y
# print(add(4,5))

# a=[[7,11],[6,4],[8,10]]
# a.sort(key=lambda a:a[1])
# print(a)

# import random
# # dev=random.randint(1,9)
# # print(dev)
# lst=["Manan", "Ketan", "Dhruv", "Mintoo"]
# choice=random.choice(lst)
# print(choice)

# me="Devendra"
# a="I am %s" %me
# print(a)

# me="Devendra"
# a1="Shakya"
# a="I am {1} {0}"
# b=a.format(me, a1 )
# print(b) 

# import math
# me="Devendra"
# a1="Shakya"
# a=f"This is {me} {a1} {math.cos(45)}"
# print(a)

# def hari(a,b,c):
#     print(a,b,c)

# hari("Manan", "Ketan", "Dhruv", "Mintoo")

# def function1(tiger, *arg1, **kwargs):
#     print(tiger)
#     for item in arg1:
#         print(f" {item} is a hero")

#     for key, value in kwargs.items():
#         print(f"{key} has alphabet {value}")  

# hari=["Dev", "Manan", "Ketan", "Dhruv", "Mintoo"]
# tiger="I am tiger"
# lion={"1":"abc", "2":"cde", "3":"efg"}
# function1(tiger, *hari, **lion)

# import time
# k=0
# initial=time.time()
# while k<45:
#     print("This is Manan")
#     k=k+1
# print("Time taken by while loop", time.time()-initial, "Seconds")

# initial2=time.time()
# for i in range(45):
#     print("This is Devendra")
# print("Time taken by for loop", time.time()-initial2, "Seconds")


# localtime=time.asctime()
# print(localtime)

# print(time.asctime())

# lst1=["Bhindi", "Aloo", "Gajar", "Baigan"]
# i=1   
# for item in lst1:
#     if i%2!=0:
#          print(f"Jarvis please buy {item}")
#     i=i+1

# for index, item in enumerate(lst1):
#     if index%2==0:
#         print(f"Jarvis please buy {item}")


# import phonenumbers
# from phonenumbers import carrier
# from phonenumbers import geocoder
# import phonenumbers.timezone
# phonenumbers.PhoneMetadata.load_all()
# a=input("Enter the Mobile no.:")
# phone_num=phonenumbers.parse(a)
# print(geocoder.description_for_number(phone_num,"en"))
# print(carrier.name_for_number(phone_num,"en"))

# import sklearn as sk
# print(sk.__version__) 

# import sys
# print(sys.path)

# from sklearn.ensemble import RandomForestClassifier
# print(RandomForestClassifier())

# import file3
# print(file3.a)

# import imp_file
# print(imp_file.tiger(" and that is me")) 

# import imp_file
# print(imp_file.tiger(" Hello its me"))

# import imp_file
# print(imp_file.add(3,4))

# lis1=["Manu", "Chanu", "Dhruv"]
# # for itme in lis1:
#     # print(itme, " and ", end="")

# # a=" and ".join(lis1)
# a=" , ".join(lis1)

# print(a, "Other boys")

# num=["7","4","6","9"]
# num=list(map(int, num))
# num[3]=num[3]+1
# print(num[3])

# def sqr(a):
#     return a*a
# num=[2,4,6,1,8,12,9]
# square=list(map(sqr, num))
# print(square)

# num=[2,4,6,1,8,12,9]
# sqr=list(map(lambda a:a*a, num))
# print(sqr)

# def sqr(a):
#     return a*a
# def cub(a):
#     return a*a*a
# lst=[sqr, cub]
# for i in range (5):
#     val=list(map(lambda x:x(i),lst))
#     print(val)  


# def flt(num):
#     return num>5
# num=[3,5,6,7,98,4]
# grtnum=list(filter(flt, num))
# print(grtnum)

# num=[3,5,6,7,98,4]
# # grtnum=list(filter(lambda x:x>5, num))
# # print(grtnum)
# print(list(filter(lambda x:x>5, num)))


# from functools import reduce
# num=[3,5,6,7,9,4]
# add_num=reduce(lambda x,y:x+y, num)
# print(add_num)

# def dec1(func1):
#    def hel1():
#       print("===========")
#       func1()
#       print("===========")
#    return(hel1)
# # dec1("Hi")  
# @dec1
# def dec2():
#    print("Who is Dev?")
# # dec2=dec1(dec2)
# dec2()

# def func1():
#    print("This is devendra")
#    return func1
# func1()


# class student:
#    No_of_leaves=8
#    pass
# dev=student()
# manu=student() 
# dev.name="Devendra"
# dev.stdr=12
# dev.school="SGM"
# dev.addrss="Kanpur"
# manu.namme="Manan"
# manu.stdr=12
# manu.school="SGM"
# dev.addrss="Jhansi"
# print(dev.__dict__)
# print(manu.__dict__)
# print(dev.No_of_leaves,",", manu.No_of_leaves)
# print(student.No_of_leaves,",", student.No_of_leaves)

# class student:
#    No_of_leaves=8

#    def prtdetail(self):
#       return f"My name is {self.name}, class is {self.stdr}, School name is {self.school} and I am from {self.addrss}."      

# dev=student()
# manu=student() 

# dev.name="Devendra"
# dev.stdr=12
# dev.school="SGM"
# dev.addrss="Kanpur"

# manu.name="Manan"
# manu.stdr=11
# manu.school="SGM"
# manu.addrss="Jhansi"
# print(manu.prtdetail())
# print(dev.prtdetail())


# class Employee:
#    def __init__(self, a, b):
#       self.name=a
#       self.locs=b
#    def prtdetails(self):
#       return f"This is my {self.name}, and from {self.locs}"

# dev=Employee("Devendra", "Jhansi")
# manu=Employee("Manan", "Kanpur")

# # dev.name="Devendra"
# # dev.locs="Jhansi"
# # manu.name="Manan"
# # manu.locs="Kanpur"
# print(dev.prtdetails())


# from tkinter import*
# root = Tk()
# def getvals():
#    print("its work")
#    print(f"{name_value.get(), phone_value.get(), gender_value.get(),emergency_value.get()}")
#    with open("records.txt", "a") as f:
#       f.write(f"{name_value.get(), phone_value.get(), gender_value.get(),emergency_value.get()}\n")
# root.geometry("500x200") 
# Label(root,text="Welcome to Lalita Travels", font="comic 13 bold").grid(row=0, column=3)
# name=Label(root, text="Name")
# phone=Label(root, text="Phone number")
# gender=Label(root, text="Gender")
# emergency=Label(root, text="Emergancy Contact")
# name.grid(row=1, column=2)
# phone.grid(row=2, column=2)
# gender.grid(row=3, column=2)
# emergency.grid(row=4, column=2)
# name_value=StringVar()
# phone_value=IntVar()
# gender_value=StringVar()
# emergency_value=IntVar()
# name_entry=Entry(root, textvariable=name_value)
# phone_entry=Entry(root, textvariable=phone_value)
# gender_entry=Entry(root, textvariable=gender_value)
# emergency_entry=Entry(root, textvariable=emergency_value)
# name_entry.grid(row=1, column=3)
# phone_entry.grid(row=2, column=3)
# gender_entry.grid(row=3, column=3)
# emergency_entry.grid(row=4, column=3)
# food_services=Checkbutton(text="Want to book your sheet?")
# food_services.grid(row=5, column=3)
# Button(text="Submit to Lalita Travels", command=getvals).grid(row=6,column=3)
# root.mainloop()

# from tkinter import*
# root=Tk()
# canvas_width=800
# canvas_height=400
# root.geometry(f"{canvas_width}x{canvas_height}")
# canvas_widget=Canvas(root, width=canvas_width, height=canvas_height)
# canvas_widget.pack()
# canvas_widget.create_line(200,0,  0,800, fill="yellow")
# canvas_widget.create_rectangle(10,200,  400,10, fill="green")
# canvas_widget.create_oval(20,300,  300,20, fill="red")
# canvas_widget.create_arc (20,40,  300,300, fill="blue")
# canvas_widget.create_text(700,20, text="Hello World")
# root.mainloop()

# from tkinter import*

# def manu(event):
#     print(f"You click on {event.x},{event.y}")

# root=Tk()
# root.title("Event count")
# root.geometry("640x400")
# btn=Button(root, text="click on me")
# btn.pack()
# btn.bind('<Button-1>', manu)
# btn.bind('<Double-1>', quit)
# root.mainloop()



# from tkinter import*
# from PIL import Image, ImageTk

# root=Tk()
# root.geometry("640x400")
# root.title("Lalita News Paper")
# list_text=[]
# photos=[]
# for i in range(0,3):
#     with open(f"file1(i+1).txt") as f:
#         text=f.read()
#         list_text.append(text)
#     image=Image.open(f"{i+1}.jpg")
#     photos.append(ImageTk.PhotoImage(image))
     
# frm1=Frame(root, width=800, height=70)
# Label(frm1, text="Lalita with news of Orai", font="Arial 33 bold").pack()
# Label(frm1, text="July-2020", font="Arial 13 bold").pack()
# frm1.pack()
# frm2=Frame(root, width=800, height=200)
# Label(frm2, text="News of Kanpur", font="Arial 33 bold").pack()
# frm2.pack()
# root.mainloop()

# list=[1,2,3,4,5,6,7,8]
# print(list[1:5])

# def anagram(str1, str2):  
#     return sorted(str1) == sorted(str2)  
  
# print(anagram('geek', 'eegk'))
# print(anagram('geek', 'peek'))


# test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4] 
# print(max(set(test), key = test.count)) 

# geek = ['Geeks', 'Programming', 'Algorithm', 'Article']
# print(geek)
# print(" ".join(geek))

# f = int(input("Enter the Number which you want factor>> "))
# print ("The factors of",f,"are")
# for i in range(1, f+1):
#    if f % i == 0:
#         print(i)




# for i in range (1,2):
#     print("*", end="")
# print()
# for i in range (1,3):
#     print("*", end="")
# print()
# for i in range (1,4):
#     print("*", end="")
# print()
# for i in range (1,5):
#     print("*", end="")
# print()

# for k in range(2,6):    
#     for i in range (1,k):
#         print("*", end="")
#     print()

# for k in range(5,1,-1):
#     for i in range (1,k):
#         print("*", end="")
#     print()

# i=0
# while i<10:
#  print(i)
#  i+=1  

# lst=["a","b","c","d"]
# lst.reverse()
# print(lst)

# lst=["a","b","c","d"]
# print(lst[::-1])

 
# itemList = ['1', '2', '3', '3', '6', '4', '5', '6']
# # newList = itemlist[]
# # [newList.append(item) for item in itemList if item not in newList]
# # print(newList)
# print(set(itemList))

# with open("davshakya.txt") as f: s = f.read()
# print (s)

# for line in reversed(list(open("davshakya.txt"))):
#     print(line.rstrip())


# t=eval("2+4+56")
# print(t)
# # help("modules")
# a = 2
# print(a)
# a=8
# b=7
# x=a+b
# print(t[1])
# print(len(t))

# k=[2,3,4,5]
# m=['24', '34', '3', '2', '23', '4', '234']
# # print(m[1])
# j=4
# for i in range(len(k)):
#     if(k[i]<j):
#         x=k[i]
#         print(list(x))
        
# j=4
# for i in range(len(k)):
#     if(k[i]<j):
#         x=k[i]
#         print(list(x))
# num="manan"
# for i in num:
#     print(i)

# num="manan"
# iter1=iter(num)
# print(next(iter1))
# print(next(iter1))

# import itertools
# st = "ABCD"
# per = itertools.permutations(st,3) 
# for val in per:
#     print(*val)


# import itertools
# st = "ABCDE"
# com = itertools.combinations(st, 3)
# for val in com:
#     print(*val)

# txt = "a b c d"
# a=2
# b=2
# c=2
# d=2
# x = txt.replace(" ", "+")
# y=eval(x)
# print(y)

# import itertools
# values = "abcd"
# com = itertools.combinations_with_replacement(values, 3)
# for val in com:
#     print(*val)







# import itertools
# values = "abcd"
# com = itertools.combinations_with_replacement(values, 3)
# for val in com:
#     # print(*val)
#     m=*val
#     txt = m
#     a=2
#     b=3
#     c=4
#     d=5
#     x = txt.replace(" ", "+")
#     y=eval(x)
#     if(y<10):
#         print(*val)

# import itertools
# values = "abcdefghij"
# com = itertools.combinations_with_replacement(values, 3)
# for val in com:
#     print(*val)

# txt = "a b c d e f g h i j "
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



# import itertools
# values = "abcdefghij"
# com = itertools.combinations_with_replacement(values, 3)
# for val in com:
#     print(*val)

# txt = "a b c d e f g h i j"
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

# import itertools
# def comb():
#     values =input("Enter any letter>>>")
#     com = itertools.combinations_with_replacement(values, 3)
#     for val in com:
#         m=print('"',*val, end='"') 
# m=comb
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

# i=0
# for i in range (5):   
#     if(i<4):
#         print (i)
#     else:
#         print("sorry")

# m="1 2 3"
# for i in range (len(m)):   
#     if(i<4):
#         print (i)
#     else:
#         print("sorry")


# import itertools
# values ="1234"
# com = itertools.combinations_with_replacement(values, 3)
# for val in com:
#     x=val
#     print(x)
    
# t=val
# for i in range (len(t)):
#  j=str(t[i])
#  def sum_str(str1):
#         sum_dgt = 0
#         for x in str1:
#             if x.isdigit() == True:
#                 z = int(x)
#                 sum_dgt = sum_dgt + z
#         return sum_dgt
# m=sum_str(t)
#   print(x)

# import itertools
# values ="1234"
# com = itertools.combinations_with_replacement(values, 3)
# for val in com:
#     t=val
#     print(t[0:3])
# # for i in range (len(t)):
# #  j=str(t[i])
# #  def sum_str(str1):
# #         sum_dgt = 0
# #         for x in str1:
# #             if x.isdigit() == True:
# #                 z = int(x)
# #                 sum_dgt = sum_dgt + z
# #         return sum_dgt
# # m=sum_str(t[i])
# # print(t)


# # import itertools
# # values ="123"
# # com = itertools.combinations_with_replacement(values, 3)
# # for val in com:
# #     t=val
# #     print(*t[0:3])

# # import itertools
# # values ="123"
# # com = itertools.combinations_with_replacement(values, 3)
# # for val in com:
# #     t=str(val)
# #     print(t[0:1])
    
# def cmb(x, y):
#     if not x: 
#         return
#     y.add(x)
#     for z in range(0, len(x)):
#         t = x[0:z] + x[z + 1:]
#         cmb(t,y)       
# y = set()
# cmb("234", y) 
# t=list(y)
# print(t)
# for i in range (len(t)):
#  j=str(t[i])
#  def sum_str(str1):
#         sum_dgt = 0
#         for x in str1:
#             if x.isdigit() == True:
#                 z = int(x)
#                 sum_dgt = sum_dgt + z
#         return sum_dgt
# m=sum_str(t[i])
# print(m)


# class Solution:
#     def search(self, candidates, target, i, res, ress):
#         if target < 0:
#             return
#         else:
#             if target == 0:
#                 res.append(ress[:]) #It is important to use "ress[:]" instead of "ress"
#             else:
#                 while i < len(candidates) and target-candidates[i] >= 0:
#                     ress.append(candidates[i])
#                     self.search(candidates, target-candidates[i], i, res, ress)
#                     i += 1
#                     ress.pop(-1) #if use "ress", this will pop the elemtnes in res also
    
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    # def combinationSum(self, candidates, target):
    #     res =[]
    #     ress = []
    #     self.search(sorted(candidates), target, 0, res, ress)
    #     return res

# 


# for a in range(5,1,-1):
#     for i in range (1,a):
#         print("*", end="")

# k=12
# j=12
# for a in range(1,k):
#     a=a+k
#     for i in range (3,a):
#         print("*", end="")
#     k=k-2
#     if k==-10:
#         break
#     print()
    
# for b in range(1,j):
#     b=b+k
#     for i in range (b,3):
#         print("*", end="")
#     j=j-2
#     if j==10:
#         break
#     print()



# f=open("test_file.txt", "r")
# content=f.read()
# print(content)







        

