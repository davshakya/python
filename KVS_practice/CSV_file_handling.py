# CSV File Handling

# Writing Data into csv file
import csv
f=open("dev_csv.csv","w+",newline='')
d=(["Name","City", "Age"])

empdata=csv.writer(f)
x=empdata.writerow(d)
for i in range(2):
    print("Employee record= ", i+1)
    Name=input("Enter employee name=")
    City=input("Enter employee City name=")
    Age=int(input("Enter employee age="))
    d=([Name,City, Age])
    x=empdata.writerow(d)
f.close()


# Reading data from CSV File  
import csv
with open("dev_csv.csv","r") as f:
    empdata= csv.reader(f)
    for i in empdata:
        print(i)


