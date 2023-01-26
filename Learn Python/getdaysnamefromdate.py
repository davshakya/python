from datetime import timedelta, date, datetime
Date_req = date.today() + timedelta(days=1)
Day_name = Date_req.strftime('%A')
print(Day_name)
day_dict={"Sunday":1,"Monday":2,"Tuesday":3,"Wednesday":4,"Thursday":5,"Friday":6,"Saturday":7,}
if day_dict[Day_name]==1:
    print(1)
else:
    print(day_dict[Day_name]+6)
