class Calc:
    def __init__(self,num1):
        self.num=num1
    def square(self):
        print(f"Square= {self.num**2}")
    def square_root(self):
        print(f"Square root= {self.num**0.5}")
    def cube(self):
        print(f"Cube= {self.num**3}")

    @staticmethod
    def great():
        print("Welcome to calculator")

sqc=Calc(4)
sqc.square()
sqc.square_root()
sqc.cube()
Calc.great()
 



 


























