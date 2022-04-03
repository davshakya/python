
################Program for LCM#################
# def lcm_pro(a,b):
#     if a>b:
#         greater=a
#     else:
#         greater=b
#     while (True):
#         if (greater%a==0) and (greater%b==0):
#             break
#         greater=greater+1
#     return greater
# x=lcm_pro(2,3)
# print(x)


################Program for Prime number #################
# n=int(input("Enter any number to check prime number= "))
# a=[]
# for i in range(1,n+1):
#     if n%i==0:
#         a.append(i) 
# if len(a)==2:
#     print("It is prime number")
# else:
#     print("It is composite number")
    
    
################Program for Armstrong number #################
# n=int(input("Enter any no. to check armstrong="))
# s=str(n)
# y=[]
# print(len(s))
# # print(s[1])
# for i in range(0,len(s)):
#     x=int(s[i])**len(s)
#     y.append(x)
# if sum(y)==n:
#     print("It is armstrong no.")


################ Febonicci number #################
#n=0,1,1,2,3,5,7,8
n=10
x=0
y=1
l=[]
for i in range(1,n):
    