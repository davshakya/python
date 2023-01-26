# def deco(func):
#     def inner():
#         print("it will print first")
#         b=func()+5
#         print("Updated value of a is=",b)
#         print("it will print first")
#     return inner

# @deco
# def func():
#     a=5
#     print("Original value of a is =",a)
#     return a
# func()




def func():
    a=5
    return a

def deco(func):
        b=func()+5
        print("Updated value of a is =",b)
deco(func)