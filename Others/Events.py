from tkinter import*
root=Tk()
root.title("Event handler")
root.geometry("800x400")
def dev(event):
    print(f"You clicked on button {event.x},{event.y}")
bt=Button(root, text="Click on me", font="Arial 10 bold")
bt1=Button(root, text="X", font="Arial 10 bold")
bt.pack()
bt1.pack()
bt.bind('<Button-1>',dev)
bt1.bind('<Button-1>',quit)
bt.bind('<Double-1>',quit)

root.mainloop()

