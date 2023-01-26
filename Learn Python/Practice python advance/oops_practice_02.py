class Employee:
    salary=1000
    increment=1.5
    @property
    def salary_incr(self):
        return self.salary*self.increment

    @salary_incr.setter
    def salary_incr(self,sai ):
        self.increment=sai/self.salary
    
e=Employee()
print(e.salary_incr)
e.salary_incr=2000
print(e.increment)
print(e.salary_incr)







