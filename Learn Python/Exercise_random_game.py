# def great(a,b,c):
#     if(a>b):
#         if(a>c): 
#             return a
#         else:
#             return c
#     else:
#         if(b>c):
#             return b
#         else:
#             return c
# print(great(7,8,9))
        
    

# ????????????????????????
#  farenhite to celcius**************************

# def cel(f):
#     return((f-32)/9)*5
    
# far=int(input("Enter the Temp in Farenhite=  "))
# f=cel(far)
# print("Temp in Celcius",f)

# ******************************************
# print("Hello!",end="  ")
# print("How",end=" ")
# print("are",end=" ")
# print("you",end=" ")

# print("Helo")
# print("How")
# print("are")
# print("you")



# **********************************************
# n=1
# def star():
#  global n
#  for k in range(5):
#      print("*"*n)
#      n=n+1    
# star()

# ***********************************************
# def star():
#  global n
#  for k in range(5):
#      print("*"*(n))
#      n=n-1
# star()

# **************************************************

# def remove_split(s):
#     return s.split()
# k=remove_split("......Hello world.....")
# print(k) 

# **************************************************

import random
j=int(input("Player's turn>> Enter any number between 1 to 5 \n>>>  "))
def game(g):
    k=random.randint(1,5)
    if k==g:
        print(("\nHurrey!!!! You Won!\n"))
    else:
        print(("\nOhooo!!!! Better luck for next time.\n"))
game(j)










