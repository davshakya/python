from tkinter import*
root=Tk()
root.geometry("300x520")
root.iconbitmap('1.ico')
root.title("Calculator by Elalita")
scvalue=StringVar()
scvalue.set(" ")
screen=Entry(root, textvar=scvalue,bg="yellow", font="lucida 35 bold")
screen.pack(fill =X,ipadx=8, padx=10, pady=10)
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if  scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as Error:
                value="Error!"
            
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
f1=Frame(root,bg="white")
b=Button(f1,text="9",padx=10, pady=10,bg="green", font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)

b=Button(f1,text="8",padx=10, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)

b=Button(f1,text="7",padx=10, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)

b=Button(f1,text="+",padx=10, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)
f1.pack()

f1=Frame(root,bg="white")
b=Button(f1,text="6",padx=11, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)

b=Button(f1,text="5",padx=10, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)

b=Button(f1,text="4",padx=11, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)

b=Button(f1,text="-",padx=12, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)
f1.pack()

f1=Frame(root,bg="white")
b=Button(f1,text="3",padx=10, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)

b=Button(f1,text="2",padx=10, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)

b=Button(f1,text="1",padx=12, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)

b=Button(f1,text="/",padx=12, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)
f1.pack()

f1=Frame(root,bg="white")
b=Button(f1,text="*",padx=10, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=RIGHT, padx=5, pady=5 )
b.bind("<Button-1>", click)
b=Button(f1,text=".",padx=12, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
b=Button(f1,text="0",padx=11, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5 )
b.bind("<Button-1>", click)
b=Button(f1,text="C",padx=11, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=RIGHT, padx=5, pady=5 )
b.bind("<Button-1>", click)
f1.pack()

f1=Frame(root,bg="white")
b=Button(f1,text="=",padx=115, pady=10,bg="green",font="lucida 20  bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f1.pack()
root.mainloop()









 

