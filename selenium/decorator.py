def deco(add):
    def inner():
        a=add()
        b=a+4
        print(b)
    return inner
@deco
def add():
    a=56
    return a
add()