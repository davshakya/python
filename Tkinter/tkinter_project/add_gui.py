from tkinter import *
root=Tk()
def add():
    res=int(a.get())+int(b.get())
    label_text.set(res)
    
label_text=StringVar()
Label(root, text="Enter first number:").grid(row=0, column=0)
Label(root, text="Enter second number:").grid(row=1,column=0)
Label(root, text="Result of Addition:").grid(row=3, sticky=W)
Label(root, text="", textvariable=label_text).grid(row=3,column=1, sticky=W)
a=Entry(root)
b=Entry(root)
a.grid(row=0,column=1)
b.grid(row=1,column=1)
c = Button(root, text="Calculate", command=add)
c.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
root.mainloop()
