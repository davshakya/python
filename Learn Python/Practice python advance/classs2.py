from typing import ContextManager


class Dev:
    t="google"
    salary=100
    def tiger(a,b):
     c=a+b
     print("Sum =" ,c)
    def lion(a,b):
     c=a+b
     print("Sum =" ,c)  

# ////////////Use of Class attribute///////////
Dev.tiger(4,3)
Dev.lion(4,8)
print(Dev.t)

# //////////Create instant attribute and print///////
# /////Manan,Ketan,Dhruv are instant object///////////

Manan=Dev()
Ketan=Dev()
dhruv=Dev()
Manan.salary=400
Ketan.salary=300
print(Manan.salary)
print(Ketan.salary)

# /////its always take default value from class attribute//////////////
print(dhruv.salary)


# ////////////Use of Class attribute///////////
print(Dev.salary)







