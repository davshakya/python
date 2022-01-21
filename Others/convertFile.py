# from tkinter import*
# root=Tk()
# root.geometry("400x300")
# root.title("Example")
# def getval():
#     print("Value of username is>>>", uservalue.get())
#     print("Value of Password is>>>", passvalue.get())    
# user=Label(root, text="Username", relief=GROOVE)
# pwd=Label(root, text="Password", relief=GROOVE)
# user.grid(column=0, row=0)
# pwd.grid(column=0, row=1)
# uservalue=StringVar()   
# passvalue=StringVar()
# userentry=Entry(root, textvariable=uservalue)
# passentry=Entry(root, textvariable=passvalue)
# userentry.grid(column=1, row=0)
# passentry.grid(column=1, row=1)
# bt=Button(root, text="submit", command=getval)
# bt.grid(column=0, row=2)  
# root.mainloop()

from tkinter import*
root=Tk()
root.geometry("400x300")
root.title("Checkbox Example")
def getval():
    print(f"{namevalue.get(), mobilevalue.get(), gendervalue.get(),paymentvalue.get()}")
    with open("records.txt", "w") as f:
     f.write(f"{namevalue.get(), mobilevalue.get(), gendervalue.get(),paymentvalue.get()}")
    
Label(root, text="Welcome to Lalita Travels...", relief=GROOVE, font="Arial 10 bold").grid(column=2,row=0)
name=Label(root, text="Name",relief=GROOVE)
mobile=Label(root, text="Mobile no",relief=GROOVE)
gender=Label(root, text="Gender",relief=GROOVE)
paymentmode=Label(root, text="Payment Mode ",relief=GROOVE)
name.grid(column=0,row=1)
mobile.grid(column=0,row=2)
gender.grid(column=0,row=3)
paymentmode.grid(column=0,row=4)

namevalue=StringVar()
mobilevalue=StringVar()
gendervalue=StringVar()
paymentvalue=StringVar()
confirmvalue=IntVar()

nameentry=Entry(root, textvariable=namevalue)
mobileentry=Entry(root, textvariable=mobilevalue)
genderentry=Entry(root, textvariable=gendervalue)
paymententry=Entry(root, textvariable=paymentvalue)

nameentry.grid(column=2,row=1)
mobileentry.grid(column=2,row=2)
genderentry.grid(column=2,row=3)
paymententry.grid(column=2,row=4)

confirmvalue=Checkbutton(text="Are you want submit your detail.")
confirmvalue.grid(column=2, row=6)
bt=Button(text="Submit to Lalita Travels ", command=getval)
bt.grid(column=2, row=7)

root.mainloop() 
