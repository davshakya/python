import csv
def csv_file():
    with open("test_file.csv","a",newline='') as obj:
        fobj=csv.writer(obj)
        fobj.writerow(['Roll','Name','Total_Marks'])
        while True:
            roll=int(input("Enter roll number: "))
            name=input("Enter name: ")
            total_marks=int(input("Enter total marks number: "))
            record=[roll,name,total_marks]
            fobj.writerow(record)
            choice=int(input("1 for Enter Mode: "+"\n""2- for Exit: "+"\n""Enter your Choice: "))
            if (choice==2):
                break

def dispaly():
    with open("test_file.csv","r") as obj:
        fobj=csv.reader(obj)
        for i in fobj:
            print(i)


def search():
    with open("test_file.csv","r") as obj:
        fobj=csv.reader(obj)
        u=input("Enter the marks: ")
        next(fobj)
        for i in fobj:
            if i[2]>=u:
                print(i)

csv_file()            
dispaly()
search() 

    