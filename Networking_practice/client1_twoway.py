import socket
import threading


s = socket.socket()
try:
    s.connect(("localhost", 1234))
    print("Client is ready and connected to server")
except:
    print("Failed to connect with server")
conn_status = True

def inc_msg():
    while conn_status:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print("Server: >>", incoming_message)

def sent_msg():
    message = input("Client1: >> ")
    message = message.encode()
    s.send(message)


thread1=threading.Thread(target=inc_msg)
thread2=threading.Thread(target=sent_msg)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


