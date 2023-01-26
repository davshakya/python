# from selenium import webdriver

# driver=webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element_by_xpath("//div[@id='divUsername']/input").send_keys("Admin")
# driver.find_element_by_xpath("//div[@id='divPassword']/input").send_keys("admin123")
# driver.find_element_by_xpath("//input[@type='submit']").click()
# x=driver.find_element_by_xpath("//a[@id='menu_dashboard_index']/b").get_attribute()
# print(x)
# driver.quit()



# n=123
# rev=0
# while n>0:
#     rem=n%10
#     print(rem)
#     rev=rev*10+rem
#     n=n//10
# print(rev)


# s="devendra"
# st=""
# for i in s:
#     st=i+st
# print(st)


# for k in range(100):
#     l=[]
#     for i in range(1,k+1):
#         if k%i==0:
#             l.append(i)
#     if len(l)==2:
#         print(k)


# import datetime
#
#
# def outer(abc):
#     def inner():
#         s=abc()+5
#         print(s)
#     return inner
# @outer
# def abc():
#     a=45
#     return a
# abc()
#
#
# dt = datetime.datetime.now()
# date_without_ms = dt.replace(microsecond=0)
# future_schedule_time = date_without_ms + datetime.timedelta(minutes=25)
#
# print(future_schedule_time)
# s="abc;abcee;dee;"
# print(len(s.split(";")))



# str1 = "I am an Indian"
# s=str1.split()
# st=""
# for i in str1.split():
#     st=i+" "+st
# print(st)


# l=[9,2,3,4,5,6,7,67]

# k=[]
# for i in range(1,len(l)+1):
#     k.append(l[-i])
# print(k)


# for i in range(len(l)):
#     for j in range(i):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

# 
# n=0
# y=0
# z=1
# while n<10:
#     x=y
#     y=z
#     z=x+y
#     n=n+1
#     print(z)


# class A:
#     def __init__(self,a):
#         self.a=a+11
#         self.b=self.a+111
#         print(self.b)
#     def xyz(self,x,y):
#         self.x=x
#         self.y=y
#         self.z=self.x+self.y
#         return self.z
# class B(A):
#     # def __init__(self):
#     #     print("it is class B")
#     def abc(self):
#         pass
# obj=B(1)
# print(obj.xyz(3,4))


lt=[9,2,3,4,5,56,6,7,17]
# lt=[6,3]
# for i in range(len(lt)-1):
#     if lt[i]>lt[i+1]:
#         lt[i],lt[i+1]=lt[i+1],lt[i]
# print(lt)

k=[]
for i in range(1,len(lt)+1):
    k.append(lt[-i])
print(k)

s="devendra"
st=""
for i in s:
    st=i+st
print(st)



















