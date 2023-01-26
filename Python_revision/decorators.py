# def mydecorator(fn):
#     def inner_function():        
#         fn()
#         print('How are you?')
#     return inner_function

# @mydecorator
# def greet():
# 	print('Hi! ', end='')
# greet()

def deco(func1):
    def innerfunc():
        print("it will execute first")
        func1()+8
        print("It will print in last")
    return innerfunc


# def this_is_siv():
#     print("Hi siv")
# this_is_siv=deco(this_is_siv)
# this_is_siv()

@deco
def this_is_siv():
    a=7
    print(a)
this_is_siv()
