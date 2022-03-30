class IRCTC:
    def __init__(self):
        user_input=input("""
                        1- Enter 1 for Train Live status
                        2- Enter 2 for PNR Status
                        3- Enter 3 to check Train Schedule\n""")
        if user_input=="1":
            print("Train Live status")
        elif user_input=="2":
            print("PNR Status")
        else:
            self.train_shecdule()
            
    def train_schedule(self):
        train_number=int(input("Enter Train number"))
    def fetch_data(self,train_no)
        data=http://indianrailapi.com/api/v2/TrainSchedule/apikey/<apikey>/TrainNumber/21999/
