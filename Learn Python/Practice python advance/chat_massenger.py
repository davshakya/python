import time

def display_time():
  print(time.strftime("%A, %d %B %Y %I:%M:%S"))

def send_message():
  recipient = input("Enter the username of the recipient: ")
  message = input("Enter your message: ")
  print("\n" + recipient + ": " + message)

def read_messages():
  print("\nAvailable messages:")
  # Display list of messages

def main_menu():
  while True:
    print("\nWelcome to the chat messenger!")
    display_time()
    print("\nWhat would you like to do?")
    print("1. Send a message")
    print("2. Read messages")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
      send_message()
    elif choice == "2":
      read_messages()
    elif choice == "3":
      break

main_menu()
