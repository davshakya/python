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
try:
    # tb="create table employee_tb(emp_id int primary key, fst_name varchar(30),lst_name varchar(30), salary int, city varchar(50))"
    # tb="show tables"
    # tb="desc employee_tb"
    # tb="insert into employee_tb(emp_id, fst_name, lst_name, salary, city) values(%s,%s,%s,%s,%s)"  
    # tp=(105,'Mint2', 'Shakya', 10000,'Orai')
    # mycursor.execute(tb,tp)
    # mydb.commit()
    tb="select * from employee_tb" 
    print("Command Executed...")
except:
    print("data error....")
mycursor.execute(tb)
for x in mycursor:
  print(x)

