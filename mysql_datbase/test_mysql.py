import mysql.connector as connector
mydb = connector.connect(
                     host = "localhost",
                     port=3306  ,
                     user = "root",
                     passwd = "tiger",
                        )  
if mydb.is_connected():                                  
    print("Connection Done")
else:
    print("Not Connected")  
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)