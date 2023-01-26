class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print("Lets add")
        return self.num+num2.num
    def __str__(self):
        return f"Decimal number: {self.num}"
    def __len__(self):
        return 1

n1=Number(3)
n2=Number(4)
n=Number(9)

sum=n1+n2
print(sum) 
print(len(n))

















