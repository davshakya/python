# ///////////Single Inheritance//////////
class Employee:
    company="Google"
    def getInfo(self):
        print(f"Name of employee is Devendra from {self.company}")
    
class Programmer(Employee):
    language="Python"
    company="Reliance"

    def great(self):
        print(f"My language is {self.language} written by {self.company}")

a=Employee()
a.getInfo()
# b=Programmer()
# b.great()   
# Employee.getInfo()
# a.great()
# b=Programmer()
# b.great()




















