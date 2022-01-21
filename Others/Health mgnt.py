"""Healt Management Program
Client Name=
Health Issue-
DOB-
Date-
Ward number-
"""
Client_name=input("Enter The name of Client-")
Client_name=input("Enter Health Issue-")
Client_name=input("Enter DOB-")
Client_name=input("Enter Date-")
Client_name=input("Enter Ward-")


f=open("file1.txt", "w")
a=f.write("Client Name-\n")
a=f.write("Health Issue-\n")
a=f.write("DOB-\n")
a=f.write("Date-\n")
a=f.write("Ward-\n")
f.close()

