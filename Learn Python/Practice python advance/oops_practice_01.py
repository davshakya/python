# ///////////////Inheritance//////////////////
class C2dVct:
    def __init__(self,i,j):
        self.iVect=i
        self.jVect=j
    def __str__(self):
        return f"{self.iVect}i+{self.jVect}j"

class C3vct(C2dVct):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kVect=k
    def __str__(self):
        return f"{self.iVect}i+{self.jVect}j+{self.kVect}k"

# v1=C2dVct(2,3)
v2=C3vct(2,3,4)
# print(v1)
print(v2)
















