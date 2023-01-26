class Employee:
    company="google"
    def get_salary(self):
        print("Your Salary is 100k")
raju=Employee()
raju.get_salary() #//////its work like >>>Employee.get_salary(raju)
# Employee.get_salary(raju)


# class Employee:
#     company="google"
#     def get_salary(self,k):
#         print(f"Your Salary is {self.income} for {self.company} in {k}")
    
#     def great(self):#if "self" function remove it will give error
#         print("You are great")
# raju=Employee()
# raju.income=200
# raju.get_salary("India")
# Manan=Employee()
# Manan.great()
 

# class Employee:
#     company="google"
#     def get_salary(self,k):
#         print(f"Your Salary is {self.income} for {self.company} in {k}")
#     @staticmethod    #we use it to remove "self" function
#     def great():
#         print("You are great")

# Manan=Employee()
# Manan.great()

















