from pandas import value_counts
def fun_name(name,*arg,**kwargs):
    print(kwargs)
    print(type(arg))
    print(name)
    for item in arg:
        print(item)
    for key,value in kwargs.items():
        print(key,value)
dev=["apple","banana","cack"]
name="ranjana"
city={"a":"orai","b":"delhi","c":"kanpur"}
fun_name(name,*dev,**city)


