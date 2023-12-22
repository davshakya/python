# class Employee:
#     name="tiger"
#     company="google"
#     salary=10000
    
#     @classmethod
#     def getinfo(cls,sal):
#         cls.salary=sal
#     def abc(self):
#         print("abc method")
        
# a=Employee()
# print(a.salary)
# a.getinfo(20000)
# print(a.salary)
# print(Employee.salary)

# print(a.abc())



class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance variables
    def show(self):
        print(self.name, self.age, Student.school_name)

    @classmethod
    def change_School(cls, name):
        cls.school_name = name

    @staticmethod
    def find_notes(subject_name):
        return ['chapter 1', 'chapter 2', 'chapter 3']

obj=Student("Devendra",37)
obj.show()





























