class Employee:
    leaves=29

    def __init__(self, name, Aschool, Astd): 
        self.name=name
        self.school=Aschool
        self.std=Astd
        
    def print_detail(self):
        return f"Name is {self.name} from school {self.school} and he is in {self.std}."
        self.Name=abc
    # def change_leaves(cls, newleaves):
    #     cls.leaves=newleaves

    def from_slash(cls, string): 
        params=string.split("/")
        return cls(params[0], params[1], params[2])
        return cls(*string.split(" "))
karan=Employee.from_slash('Manan SGM 1st')
print(karan.std)
(hary.std)







