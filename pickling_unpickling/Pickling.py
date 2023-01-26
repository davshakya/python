import pickle

class Students:
    def __init__(self,name , roll, addr):
        self.name=name
        self.roll=roll
        self.addr=addr

    def display(self):
        print(f"name:{self.name} roll:{self.roll} add:{self.addr}")

with open("student_file.dat","wb+") as f:
    stud1=Students("Ajay",101,"Kanpur")
    stud2=Students("Vijay",102,"Orai")
    pickle.dump(stud1,f)
    pickle.dump(stud2,f)
    print("Pickling done!!!")

with open("student_file.dat","rb+") as f:
    obj1=pickle.load(f)
    obj2=pickle.load(f)

    print("unpickling done!!!")
    obj1.display()
    obj2.display()


