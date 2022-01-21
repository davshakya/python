from tkinter import *
root = Tk()
yourData = "My text here"
frame = Frame(root)
frame.grid()
lab = Label(frame,text=yourData)
lab.grid()
root.mainloop()