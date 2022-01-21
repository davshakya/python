import mysql.connector as connector
from mysql.connector import cursor
# import mysql.connector
# con=connector.connect(host='localhost', port='3306', user='root',
#                   password='', database='mysql_python')
# print(con)
# print(con.connection_id)

# class DBHelper:
#     def __init__(self) -> None:
#         self.con=connector.connect(host='localhost', port='3306', user='root',
#                   password='', database='mysql_python')
#         query='creat table if not exist user(userId int primary key, userName varchar(200), phone varchar=(12))'
#         cur=self.con.cursor()
#         cur.execute(query)
#         print("Created")
# helper=DBHelper()


# mydb =connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE shakya_DB")
# print(cursor)




mydb =connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)



