class Dad:
    ball=1
class Son(Dad):
    dance=1
    def isdance(self):
        return f"Yes i dance {self.dance} no of type"

class Grandson(Son):
    dance= 6
    def isdance(self):
        return f"Yes i dance {self.dance} no of type"
darry=Dad()
sarry=Son()
garry=Grandson()
print(garry.isdance())





