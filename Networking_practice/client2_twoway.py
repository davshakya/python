import socket

s = socket.socket()
try:
    s.connect(("localhost", 1234))
    print("Connected to server")
except:
    print("Failed to connect server")
conn_status = True
while conn_status:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server: >>", incoming_message)
    message = input("Client2: >> ")
    message = message.encode()
    s.send(message)
