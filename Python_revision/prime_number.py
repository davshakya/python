
# def check_prime(x):
#     lst=[]
#     for i in range(1,x+1):
#         if x%i==0:
#             lst.append(i) 
#     if len(lst)==2:
#         print(p,"is a prime number")
#     else:
#         print(p,"is composite number number")
# p=int(input("Enter any number to check whether it is prime or not  = "))     
# check_prime(p)       


n=6
l=[]
for i in range (1,n+1):
    if n%i==0:
        l.append(i) 
if len(l)==2:
    print("It is Prime Number")
else:
    print("Composite number")
