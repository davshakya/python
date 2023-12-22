import socket

ob = socket.socket()
# ob.bind(('localhost', 2301))
ob.bind(('192.168.1.43', 2301))
ob.listen()
client_obj, add = ob.accept()
print("Server is ready to accept connection")
print("connected with add:", add)
conn = True
while conn:
    msg_from_client = client_obj.recv(1024)
    msg_from_client.decode('utf-8')
    print(msg_from_client)
    if msg_from_client == b"no":
        conn = False
        ob.close()
