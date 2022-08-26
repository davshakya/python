class Tiger:
    def __init__(self):
        self.a = 9
        self.b = 8
        print("Hi Dev")

    def multi(self):
        x = self.a * self.b
        print(x)


class Abc(Tiger):
    def __init__(self):
        super().__init__()
        self.a = 9
        self.b = 8
        print("Hi Shakya")

    def addittion_add(self, i, j):
        sum1 = i + j
        print(sum1)

    def summation(self):
        self.multi()
        super().multi()
        print(self.a)
        print(self.b)


obj = Abc()
obj.addittion_add(2,3)
obj.summation()

#
# class A:
#     i=30
#     j=40
#     def xyz(self):
#         self.a=10
#         self.b=20
#         print("Hello A.xyz")
#     def abc(self):
#         print('Hello A.abc')
#         sum=self.i+self.j
#         print(sum)
#
# class B(A):
#     def abc(self):
#         super().xyz()
#         super().abc()
#         c=self.a+self.b
#         k=self.i+self.j
#         print(c,k)
# obj=B()
# obj.abc()
