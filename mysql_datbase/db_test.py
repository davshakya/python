# importing required library 
import mysql.connector 
 
# connecting to the database 
dataBase = mysql.connector.connect
                     host = "localhost",
                     user = "root",
                     passwd = "tiger",
                     database = "students" )  
 
# preparing a cursor object 
cursorObject = dataBase.cursor() 
# creating table  
studentRecord = """CREATE TABLE Employee ( 
                   NAME  VARCHAR(20) NOT NULL, 
                   BRANCH VARCHAR(50), 
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5), 
                   AGE INT
                   )"""
 
# table created
cursorObject.execute(studentRecord)  
 
# disconnecting from server
dataBase.close()