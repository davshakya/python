from tkinter import *
root=Tk()
def table():

    for x in range(11):
        i=1
        x=x*i
        i=i+1
        label_text.set(x)
label_text=StringVar()
Label(root, text="Enter any number for print table:").grid(row=0, column=0)
Label(root, text="Result:").grid(row=3, sticky=W)
Label(root, text="", textvariable=label_text).grid(row=3,column=1, sticky=W)
a=Entry(root)
b=Entry(root)
a.grid(row=0,column=1)
c = Button(root, text="Calculate", command=table)
c.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
root.mainloop()





