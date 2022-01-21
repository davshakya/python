from tkinter import * 
root=Tk()
root.title("Employee management system")
root.geometry('800x500')

f=open("sample_test.txt","w")
f.write("Hello  davshakya")
f=open("sample_test.txt","r")
print(f.read())
f.close()

Label(root, text='First Name').grid(row=0)
Label(root, text='Last Name').grid(row=1)
Label(root, text='Total').grid(row=2)

Entry(root).grid(row=0, column=1)
Entry(root).grid(row=1, column=1)
Entry(root).grid(row=2, column=1)

Button(root, text='Stop', width=25, command=root.destroy).grid(row=8,column=5)
root.mainloop()




