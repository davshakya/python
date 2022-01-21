# '''Author=Lalita Eterprises
# Lienced=ABC Company'''
# # import os
# # print("Hello world")

# # a=True
# # print(type(a))  

# # a=34
# # b=22
# # a-=2
# # b+=3
# # print(a)
# # print(b)

# # a=45>4 
# # b=45!=56
# # c=0|0
# # d=0&1
# # print(a)
# # print(b)
# # print(c)
# # print(d)

# # a=int(input("Enter any Number: "))
# # b=int(input("Enter any Number: "))
# # print(a+b)

# # greeting="Good Morning"
# # Name ="Devendra"
# # c=greeting+Name
# # print(c)
# # print(Name[0])
# # print(len(Name))
# # print(Name[0:4])
# # print(Name[0:8:2])
# # print(Name[::-1])

# # import smtplib  
# # # Calling SMTP  
# # s = smtplib.SMTP('smtp.gmail.com', 587)  
# # # TLS for network security  
# # s.starttls()  
# # # User email Authentication  
# # s.login("davshakya@gmail.com, "devrjn21#")  
# # # message to be sent  
# # message = "Message_you_need_to_send"  
# # # sending the mail  
# # s.sendmail("davshakya@gmail.com", "davshakya@hotmail.com", message)  


# import time 
  
# start = time.time() 
# count = 0
# with open("davshakya.txt") as file: 
#     for line in file: 
#        print(line) 
#        count = count + 1
# end =  time.time() 
# print("Execution time in seconds: ",(end-start)) 
# print("No of lines printed: ",count) 

numbers = [1,2,3,4,5,6,7]
evens = [x for x in numbers if x % 2 is 0]
odds = [y for y in numbers if y not in evens]

cities = ['London', 'Dublin', 'Oslo']

def visit(city):
    print("Welcome to "+city)
for city in cities:
    visit(city)

# import wikipedia

# result = wikipedia.page('freeCodeCamp')
# print(result.summary)

# for link in result.links:
#     print(link)


# keys = ['a', 'b', 'c']
# vals = [1, 2, 3]
# zipped = dict(zip(keys, vals))