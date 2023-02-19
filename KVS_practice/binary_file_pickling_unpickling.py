# "Writing data in binary file is called pickling 
import pickle
fb=open("dev_binary_file.dat","wb+")
d={"Name":"Dev","City":"Orai", "Age":37}
pickle.dump(d,fb)
print("Data write succefully")

# Reading data from binary file is call unpickling
import pickle
fb=open("dev_binary_file.dat","wb+")
reading_data=pickle.load(fb)
print(reading_data)
fb.seek(20,0)
print(fb.tell())
x=fb.read()
print(x)

