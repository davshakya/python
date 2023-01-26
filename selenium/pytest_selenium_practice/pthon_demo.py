# i=0
# l=[]
# while i<=5:
#     a=int(input("Enter value of a"))
#     i=i+1
#     l.append(a)
# print(l)
# print(tuple(l))

# t=(2,4,6)
# st={77,78,2,9,777774,7,78,783}
# # st.pop()
# # st.discard(7)
# st1={1,6}
# st.update(st1)
# print(st)

# from audioop import mul
# import multiprocessing
# print(multiprocessing.cpu_count())
# s=multiprocessing.current_process()
# print(s)

# import socket
# hostname=socket.gethostname()
# ip=socket.gethostbyname(hostname)
# print(ip)

# s="pynative"
# for i in range(len(s)):
#     if i%2==0:
#         print(s[i])
# 


# str_x = "Emma is good developer. Emma is a writer"
# s=str_x.split()


# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5


# l=[]
# for i in range(6):
#     for j in range(i):
#         l.append(i)
#         print(i,end=" ")
#     print("\n")
# print(l)


# for i in range(1,6):
#     for j in range(i):
#         print("j=",j,end=" ")
#     print("When i=",i,"\n")


# Number = 123   
# Reverse = 0    
# while(Number > 0):    
#     Reminder = Number %10   
#     Reverse = (Reverse *10) + Reminder    
#     Number = Number //10    
# print("Reverse of entered number is = %d" %Reverse)


# st={23,3,45,5}
# print(st)
# x=st.copy()
# del st
# print(x)


# x=25
# def func():
#     global x
#     x=x+1
#     print(x)

# func()
# print(x)

# print(",".join(['jdoe is', 42, 'years old']))



# x=print(*['jdoe is', 42, "abc", 'years old'])

# from itertools import cycle
# from time import sleep
# for frame in cycle(r'-\|/-\|/'):
#     print('\r', frame, sep='', end='', flush=True)
#     sleep(0.2)

# from time import sleep
# def progress(percent=0, width=30):
#     left = width * percent // 100
#     right = width - left
#     print('\r[', '#' * left, ' ' * right, ']',f' {percent:.0f}%', sep='', end='', flush=True)

# for i in range(101):
#     progress(i)
#     sleep(0.1)


# print("Hello %s"%"Devendra")
# print("Hello %s"%"Devendra")
# print("Hi %f"%6.5)

# print(type("sdf"))

# print(3*2%3)
# d=dict()
# print(d=={})
# d.update({2:1})
# l=list()
# print(l==[])
# l.append(3)
# s=set()
# print(s=={})
# s.add(4)
# t=tuple()
# print(t==())
# print(d,l,s,type(t))

# class A:
#     def __init__(self,i=100):
#         self.i=i

# class B(A):
#     def __init__(self,j=100):
#         self.j=j
#         x=self.i+self.j



# def main():
#     b=B()
#     a=A()
#     print(a.i)
#     print(b.j)
#     print(b.x)
# main()


class A:

    x=30
    def __init__(self,i=100):
        print("This is constructor of class A ")

    def func1(self):
        self.i=100
        print("This class A")
        # print(self.x)


class B:

    def __init__(self,j=100):
        super().__init__()
        print("This is constructor of class B ")

    def func2(self):
        self.j=200
        print("This class B")
        # print(self.i+self.j)


class C(A,B):

    def __init__(self,j=100):
        print("This is constructor of class C ")

    def func3(self):
        super().func1()
        super().func2()
        print("This class C")
        print(self.x)
        print(self.i+self.j)



b=C()
b.func3()



