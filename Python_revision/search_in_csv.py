import csv
def search():
    with open("test_file.csv","r") as obj:
        fobj=csv.reader(obj)
        u=input("Enter the value: ")
        next(fobj)
        for i in fobj:
            if i[2]>=u:
                print(i)
search()

 