from tkinter import ttk
from tkinter import *

root = Tk()

pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
pb.pack()
pb.start()

root.mainloop()