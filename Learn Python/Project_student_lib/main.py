a=input("Enter the name of patient: ")
b=input("Enter the age of patient: ")
c=input("Enter DOB in DD-MM-YYYY: ")

f=open("std_lib.txt","w")
f.write("Name:"+a+"\n" "Age: "+b+"\n""Date of Birth: "+c)
f=open("std_lib.txt","r")
print(f.read())
f.close()




