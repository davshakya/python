from tkinter import*
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("750x450")
root.title("Radio Button")

var =IntVar()
# var.set(1)
Label(root,text="What would you like sir ?", font="lucida 19 bold", justify=RIGHT, padx=10).pack()
radio=Radiobutton(root, text="Dosa", font="lucida 10 bold", padx=10, variable=var, value=1).pack()
radio=Radiobutton(root, text="Rosgulla", font="lucida 10 bold", padx=10, variable=var, value=2).pack()
radio=Radiobutton(root, text="Paneer", font="lucida 10 bold", padx=10, variable=var, value=3).pack()
radio=Radiobutton(root, text="Aalu Paratha", font="lucida 10 bold", padx=10, variable=var, value=4).pack()
root.mainloop()



