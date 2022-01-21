from tkinter import *
import pymongo
from pymongo import MongoClient
root = Tk()
client= MongoClient("mongodb+srv://mongodb_user:tiger@cluster0.2xict.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.get_database("employee")
records=db.emp_record
total_db=client.list_database_names()
r=records.find_one({"name":"Manav"})
w = Label(root, text=total_db)
y = Label(root, text=r)
y.pack()
w.pack()
root.mainloop()










