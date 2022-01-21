from tkinter import *
import pymongo
from pymongo import MongoClient
root = Tk()
client= MongoClient("mongodb+srv://mongodb_user:tiger@cluster0.2xict.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.get_database("employee")
records=db.emp_record
r=records.find_one({"name":"Manav"})

w = Label(root, text=r)

w.pack()
root.mainloop()  