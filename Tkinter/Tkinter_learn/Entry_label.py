from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
Entry(master).grid(row=0, column=1)
Entry(master).grid(row=1, column=1)

mainloop()