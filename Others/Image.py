from tkinter import*
from PIL import Image, ImageTk
root=Tk()
root.title("Images file")
root.geometry("500x300")
image = Image.open("msc.jpg")
pic = ImageTk.PhotoImage(image)
# nat=Label(image=pic)
# nat.pack()
root.mainloop()

