class Employee:
    name="tiger"
    company="google"
    salary=10000
    @classmethod

    def getinfo(cls,sal):
        cls.salary=sal
        
a=Employee()
print(a.salary)
a.getinfo(20000)
print(a.salary)
print(Employee.salary)



































