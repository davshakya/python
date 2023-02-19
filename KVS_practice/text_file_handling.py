f=open("dev.txt","w+")
# input_text=input("Enter any text >> ")
# f.write(input_text)
f.write("Hello Dev Shakya")
print(f.tell())
f.seek(0)
x=f.read()
print(x)
f.seek(10)
x=f.read()
print(x)
f.flush()
f.close()






