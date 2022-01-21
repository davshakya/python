
# with open("sample1.txt", "w") as g:
#     b=g.write("hello Manan shakya")
# with open("sample1.txt", "r") as f:
#     a=f.read()
#     print(a) 
# if "Manan" in a:
#     print("Yes present")
# else:
#     print("Not Present")

# ///////////////////Search text in file///////////////////

content=True
n=1
with open ("davshakya.txt", "r") as f:
   while content:
    content=f.readline()
    if "abigf" in content:
        print(n,content)
    n+=1
    



