import socket

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
while conn_status:
    message = input("Server: >> ")
    message = message.encode()
    conn.send(message)

    incoming_msg = conn.recv(1024)
    incoming_msg = incoming_msg.decode()
    print("Client: >> ", incoming_msg)


