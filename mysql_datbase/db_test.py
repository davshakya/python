import mysql.connector as mysql_cnt
mydb = mysql_cnt.connect(
                     host = "localhost",
                     port=3306,
                     user = "root",
                     passwd = "tiger",
                     database="employee"
                        )  
if mydb.is_connected():                                  
    print("Connection Done")
else:
    print("Not Connected")  
mycursor = mydb.cursor()

    
tb="insert into employee_tb(emp_id, fst_name, lst_name, salary, city) values(%s,%s,%s,%s,%s)"  
tp=(104,'Dhruv', 'Verma', 30000,'Orai')
mycursor.execute(tb,tp)
mydb.commit()
print("Command Executed...")
