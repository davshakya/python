'''Multi level Inheritence'''
# class A():
#     def displayA(self):
#         print("It is class A")
# class B(A):
#     def displayB(self):
#         print("It is class B")      
# class C(B):
#     def displayC(self):
#         print("It is class C")      
# obj=C()
# obj.displayA()
# obj.displayB()
# obj.displayC()


"""Multiple Inheritence"""
class A():
    def displayA(self):
        print("It is class A")
class B():
    def displayB(self):
        print("It is class B")      
class C(A,B):
    def displayC(self):
        print("It is class C")      
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()







