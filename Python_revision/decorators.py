def mydecorator(fn):
    def inner_function():        
        fn()
        print('How are you?')
    return inner_function

@mydecorator
def greet():
	print('Hi! ', end='')
greet()

