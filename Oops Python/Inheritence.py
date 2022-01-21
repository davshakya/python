class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod 
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class programmer(Employee):
    def __init__(self, aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages 

    def printprog(self):
        return f"The Name is {self.name}. Salary is {self.salary}, and role is {self.role}, and Languages are{self.languages}"
    


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

subham=programmer("Subham", 555, "programmer", ["JAVA","C++"])
karam=programmer("Karam", 444, "programmer", ["python"])
print(karam.printprog()) 
print(subham.printprog()) 
Employee.printgood("Rohan")





