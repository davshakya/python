from tkinter import*
root = Tk()
def getvals():
   # print(f"{name_value.get(), phone_value.get(), gender_value.get(),emergency_value.get()}")
   f=open("records_excel.csv", "a")
   f.write(f"{name_value.get(), phone_value.get(), gender_value.get(),emergency_value.get()}\n")
   f=open("records_excel.csv", 'r')
   data_sheet.set(f.read())

data_sheet=StringVar()
Label(root,text="Welcome to Lalita Travels", font="comic 13 bold").grid(row=0, column=3)
Label(root, text="Name").grid(row=1, column=2)
Label(root, text="Phone number").grid(row=2, column=2)
Label(root, text="Gender").grid(row=3, column=2)
Label(root, text="Emergancy Contact").grid(row=4, column=2)
Label(root, text="", textvariable=data_sheet).grid(row=8, column=3)

name_value=StringVar()
phone_value=IntVar()
gender_value=StringVar()
emergency_value=IntVar()
name_entry=Entry(root, textvariable=name_value).grid(row=1, column=3)
phone_value=Entry(root)
phone_value.grid(row=2, column=3)
gender_entry=Entry(root, textvariable=gender_value).grid(row=3, column=3)
emergency_value=Entry(root)
emergency_value.grid(row=4, column=3)
food_services=Checkbutton(text="Want to book your sheet?").grid(row=5, column=3)
button=Button(text="Submit to Lalita Travels", command=getvals).grid(row=6,column=3)
root.mainloop()








