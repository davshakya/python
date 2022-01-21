import pymongo
from pymongo import MongoClient


client= MongoClient("mongodb+srv://mongodb_user:tiger@cluster0.2xict.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.get_database("employee")
records=db.emp_record
a=records.count_documents({})
print(a)
print(client.list_database_names())

# new_emp={"name":"Manav",
# "age":22,
# "emp":456}
# records.insert_one(new_emp)
r=records.find_one({"name":"Manav"})
print(r)
























