class Employee():
    no_of_leave=8 
    def __init__(self, aname, arole, asalary):
        self.name=aname
        self.role=arole
        self.salary=asalary
    def printdetails(self):
        return f"Name is {self.name}, his role is {self.role} and salary is {self.salary}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leave=new_leaves
    

manu=Employee("Manan", "Manager", 50000)
chanu=Employee("Manav", "Engineer", 70000)   
print(manu.__dict__)
print(chanu.__dict__)
print(manu.salary)
manu.change_leaves(34)
print(manu.no_of_leave)
