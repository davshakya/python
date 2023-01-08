# def fibonacci(n):
#   a, b = 0, 1
#   for i in range(n):
#     a, b = b, a + b
#     yield a


# for i in fibonacci(10):
#   print(i)


0,1,1,2,3,5,8
a=0
b=1
# n=int(input("Enter any number to print series ="))
for i in range(10):
    
    c=a+b
    a=b
    b=c
    
    print(c)