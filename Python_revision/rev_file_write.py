# fobj=open("2.txt",'a')
# inp=int(input("Enter Number of Student "))
# for i in range(inp):
#     std=input("Enter Name of Student ")
#     cls=(input("Enter Name of Class "))
#     dtl="Student Name:- "+std, "class:- " +cls
#     fobj.write(str(dtl)) 
#     fobj.write("\n")
# fobj.close()


fobj=open("2.txt",'a')
inp=int(input("Enter Number of Student "))
for i in range(inp):
    std=input("Enter Name of Student ")
    cls=(input("Enter Name of Class "))
    fobj.write("Name student:-"+std+"\n")
    # fobj.write("\n")
    fobj.write("Name class:-"+cls+"\n") 
    fobj.write("\n")
fobj.close()











