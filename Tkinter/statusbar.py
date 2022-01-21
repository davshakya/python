from tkinter import*
root=Tk()
root.title("StatusBar Tutorial")
root.geometry("700x450")
def upload():
    strvar.set("Busy")
    sbar.update()
    import time
    time.sleep(2)
    strvar.set("Ready Now")
strvar=StringVar()
strvar.set("Ready")
sbar=Label(root, textvariable=strvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root,text="Upload", command=upload).pack()



root.mainloop()


  