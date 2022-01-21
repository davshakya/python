import mysql.connector as connector
# mydb = connector.connect(
#                      host = "localhost",
#                      user = "root",
#                      passwd = "tiger",)  
# cur=mydb.cursor()
# cur.execute("CREATE DATABASE DB1")


# import mysql.connector as connector
# mydb = connector.connect(
#                      host = "localhost",
#                      user = "root",
#                      passwd = "tiger",
#                      database = "DB1" )  
# cur=mydb.cursor()
# t1=cur.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# cur.execute(t1)


# import mysql.connector as connector
# mydb = connector.connect(
#                      host = "localhost",
#                      user = "root",
#                      passwd = "tiger",
#                      database = "DB1" )  
# cur=mydb.cursor()
# t2="INSERT INTO customers(name, address) VALUES(%s,%s)"
# b1=("Raju", "Orai")
# cur.execute(t2,b1)
# mydb.commit()


# mydb = connector.connect(
#                      host = "localhost",
#                      user = "root",
#                      passwd = "tiger",
#                      database = "DB1" )  
# cur=mydb.cursor()
# t2="INSERT INTO customers(name, address) VALUES(%s,%s)"
# b1=[("Raju", "Orai"), ("Manan", "Jalaun"), ("Manav", "Orai1"), ("Dhruv", "Konch")]
# cur.executemany(t2,b1)
# mydb.commit()


mydb = connector.connect(
                     host = "localhost",
                     port=3307,
                     user = "root",
                     passwd = "tiger",
                     database = "shakya" )  
cur=mydb.cursor()
s1="SELECT * FROM employee"
cur.execute(s1)
result=cur.fetchall()
for rec in result:
    print(rec)


# mydb = connector.connect(
#                      host = "localhost",
#                      user = "root",
#                      passwd = "tiger",
#                      database = "DB1" )  
# cur=mydb.cursor()
# upd="UPDATE customers SET title=orai+jalaun, WHERE title==orai1"
# cur.execute(upd)
# mydb.commit()


# mydb = connector.connect(
#                      host = "localhost",
#                      user = "root",
#                      passwd = "tiger",
#                      database = "DB1" )  
# cur=mydb.cursor()
# dlt="DELETE FROM customers WHERE name='Raju'"
# cur.execute(dlt)
# mydb.commit()













