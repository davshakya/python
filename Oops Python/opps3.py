class Employee:
    def __init__(self, name, school):
        self.name=name
        self.school=school
    def in_details(self):
        return f"My name is {self.name} and i am studying in {self.school}."
    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
p1 = Employee.from_dash("Devendra-SGM")
print(p1.name)
print(p1.school)
print(p1.in_details())
