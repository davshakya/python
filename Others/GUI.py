from tkinter import *
# from tkinter import ttk
from PIL import Image, ImageTk
root=Tk()   
root.geometry("350x200")
lbl=Label(text="Nature is Almighty")
lbl.pack()
image=Image.open("wall.jpg")
pic=ImageTk.PhotoImage(image=Image.open("wall.jpg"))
nature=Label(image=pic)
nature.pack()
root.mainloop()

