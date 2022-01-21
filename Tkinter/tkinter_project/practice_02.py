import tkinter as tk
from tkinter.constants import LEFT
window = tk.Tk()
frame1 = tk.Frame(master=window, width=100,height=100, bg="red")
frame1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
frame2 = tk.Frame(master=window, width=50, bg="yellow")
frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
frame3 = tk.Frame(master=window, width=25, bg="blue")
frame3.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
window.mainloop()













