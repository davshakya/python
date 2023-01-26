# /////////Multilevel inheritenace///////////////
class Employee:
    company="google"
    def info(self):
        print("I am breathing....")
class Person(Employee):
    company="Reliance"
    def info(self):
        super().info()
        print("I am working")
class GetInfo(Person):
    company="Ericsson"
    def info(self):
        super().info()
        print("I am a programmer")

a=Employee()
b=Person()
c=GetInfo()
a.info()
b.info()
c.info()














