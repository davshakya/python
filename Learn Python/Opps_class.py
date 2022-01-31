# class DemoClass():
#     a=3    
# obj=DemoClass()
# obj1=DemoClass()
# print(obj.a)
# print(obj1.a)


# class DemoClass():
#     a=3    
#     def sumvalue(self):
#         print(20*30)        
# obj=DemoClass()
# print(obj.a)
# obj.sumvalue()


# class DemoSelf():
#     a=10
#     def sumvalue(self):
#         print(self.a)
#     def info(slef,i,j):
#         print(i*j)   
#     def msg(self):
#         print("Welcome python")     
# obj=DemoSelf()
# obj.sumvalue()
# obj.info(3,2)
# obj.msg()


class DemoSelf():
    a=10
    def __init__(self):
        print("It is contructor")
obj=DemoSelf()