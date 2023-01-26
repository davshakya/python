class Employee:
    company="google"
    def get_salary(self,k,l):
        print(f"Your Salary is {self.income} for {self.company} in {k},{l}")
 
    @staticmethod    #we use it to remove "self" function
    def great():
        print("You are great")

    @staticmethod    #we use it to remove "self" function
    def time():
        print("Its 9:00 AM in the morning")

raju=Employee()
raju.income=200
raju.get_salary("Orai", "India")
Manan=Employee()
Manan.great()
morning=Employee()
morning.time()