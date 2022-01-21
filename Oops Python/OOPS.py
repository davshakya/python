# class Employee:
#     pass
#     def print_detail(self):
#         return f"Name is {self.Name} from school {self.school} and he is in {self.std}."
# hary=Employee()
# rohan=Employee()

# hary.Name="Manan Shakya"
# hary.school="SN Gupta Konch"
# hary.std="1st class"
# rohan.Name="Kartavya Shakya"
# rohan.school="SN Gupta  School"
# rohan.std="LKG class"
# print(hary.print_detail())
# print(hary.Name) 

class Employee: 
    leaves=29
    def __init__(self, Aname, Aschool, Astd): 
        self.Name=Aname
        self.school=Aschool
        self.std=Astd
        
    def print_detail(self):
        return f"Name is {self.Name} from school {self.school} and he is in {self.std}."
    def change_leaves(cls, newleaves):
        cls.leaves=newleaves

hary=Employee("Manan Shakya","SN Gupta Konch","1st class")
rohan=Employee("Kartavya Shakya","SN Gupta School","LKG class" )
print(hary.print_detail())
print(hary.std) 
hary.change_leaves(34)
print(hary.leaves)  
