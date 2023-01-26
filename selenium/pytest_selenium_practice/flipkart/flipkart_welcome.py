import sys
from flipkart_db import Mysql_db


class Flipkart:
    def __init__(self):
        self.db = Mysql_db()
        self.welcome_page()

    def welcome_page(self):
        print("""
         Select below options
         Press 1 for Registration
         Press 2 for login 
         Press 3 for exit \n""")
        s = input()
        if s == "1":
            self.registration()
        elif s == "2":
            self.login()
        elif s == "3":
            sys.exit()
        else:
            print("Invalid Input, Please try again")
            self.welcome_page()

    def login_menu(self):
        print("""
        Enter 1 to see profile
        Enter 2 to edit profile
        Enter 3 to delete profile
        Enter 4 to logout profile
        """)

    def registration(self):
        name = input("Enter user_name ")
        email = input("Enter user email id ")
        password = input("Enter user password ")
        response = self.db.register(name, email, password)
        if response == 1:
            print("Registration Successfully")
        else:
            print("Registration failed")
        self.welcome_page()

    def login(self):
        email = input("enter email ")
        password = input("enter password ")
        data = self.db.search(email, password)
        if len(data) == 0:
            print("Invalid email/password")
            self.login()
        else:
            print("Welcome", data[0][1])
            self.login_menu()

obj_wl = Flipkart()
