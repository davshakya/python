import mysql.connector as connector
mydb = connector.connect(
                     host = "localhost",
                     port=3306,
                     user = "root",
                     passwd = "tiger",
                     database = "students" )  
if mydb.is_connected():                                  
    print("Connection Done")
else:
    print("Not Connected")  

cur=mydb.cursor()
s1="SELECT * FROM student"
cur.execute(s1)
result=cur.fetchall()
for rec in result:
    print(rec)


# # cur=mydb.cursor()
# s1="SELECT name FROM employee where id=8"
# cur.execute(s1)
# result=cur.fetchall()
# for rec in result:
#     print(rec)  

# # cur=mydb.cursor()
# s1="SELECT * FROM employee where id=14"
# cur.execute(s1)
# result=cur.fetchall()
# x=list(result)
# print(x)