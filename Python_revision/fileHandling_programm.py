std=int(input("Enter the number of student "))
fobj=open("student.txt","a")
for i in range(std):
    Name=input("Enter the name of student ")
    Age=input("Enter the Age of student ")
    Class_name=input("Enter the Class of student ")
    Contact=input("Enter the Contact No. of student ")
    City=input("Enter the City of student ")
    detail="Name:- "+ Name+"\n" "Age:-"+Age+"\n" "Class_name:- "+Class_name+"\n" "Contact:-"+Contact+"\n" "City:- "+City+"\n"
    fobj.write(detail) 
    fobj.write("\n")
fobj.close()
print("Programm run succesfully")
 


