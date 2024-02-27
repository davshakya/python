import socket
import threading

s = socket.socket()
try:
    s.bind(("localhost", 1234))
    print("Server is ready")
except:
    print("Server is not ready")
s.listen()
conn, add = s.accept()
print(add, "has connected")
conn_status = True

def send_msg():
    while conn_status:
        message = input("Server: >> ")
        message = message.encode()
        conn.send(message)

def inc_msg():
    incoming_msg = conn.recv(1024)
    incoming_msg = incoming_msg.decode()
    print("Client: >> ", incoming_msg)


thread1 = threading.Thread(target=inc_msg)
thread2 = threading.Thread(target=send_msg)
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()