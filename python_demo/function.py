# def outer(abcd):
#     def inner():
#         k = abcd()
#         x = k + 5
#         print(x)
#     return inner
# @outer
# def abcd():
#     a = 5
#     return a
#
#
# abcd()
# # print(abc())


# def multiply(a,b):
#     result=0
#     if b==1:
#         return a
#     else:
#         return a+multiply(a,b-1)
# print(multiply(3,4))

# def factorial(a):
#     if a<=0:
#         return 1
#     else:
#         return a*factorial(a-1)
# print(factorial(4))


def fibonacci(n):

    x=0
    y=1
    z=0
    while n>0:
            x=y
            y=z
            z=x+y
            n=n-1
            yield z
print(list(fibonacci(12)))


def fib(m):
    if m==0 or m==1:
        return 1
    else:
        return fib(m-1)+fib(m-2)
print(fib(3))




