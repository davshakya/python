class Employee:
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
karan = Employee.from_dash("Karan-480-Student")
print(karan.salary)

