# ////////////Multiple Inheritance///////////

class Employee:
    company="Google"
    
class Language:
    company="Reliance"
    name="Devendra"


class Programmer(Employee, Language):
    def great(self):
        print(f"Im in {self.company} and my name is {self.name}")

a=Programmer()
print(a.company)
a.great()




