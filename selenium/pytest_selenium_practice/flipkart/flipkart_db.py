import mysql.connector as mysql


class Mysql_db:

    def __init__(self):
        try:
            self.mydb = mysql.connect(user="root", host="localhost", password="", database="doodledemo")
            self.my_cursor = self.mydb.cursor()
            print("Database connected...")
        except:
            print("Database connection not established.")

    def register(self, name, email, password):
        try:
            sql = f"insert into employee values(null,'{name}','{email}','{password}');"
            self.my_cursor.execute(sql)
            self.mydb.commit()
        except:
            return -1
        else:
            return 1

    def search(self, email, password):
        self.my_cursor.execute(f"select * from employee where email like '{email}' and password like '{password}'")
        data = self.my_cursor.fetchall()
        return data


obj = Mysql_db()
