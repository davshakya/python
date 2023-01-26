class Employee:
    name="Devendra"
    salary=1200
    PF=800
    @property
    def total_salary(self):
        return self.salary+self.PF

    @total_salary.setter
    def total_salary(self,val):
        self.PF=val-self.salary

e=Employee()
print(e.total_salary)
e.total_salary=1400
print(e.salary)
print(e.PF)






























