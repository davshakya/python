import socket

ob = socket.socket()
ob.connect(('localhost', 2301))
# msg = "hello this is first client"
# ob.send(msg.encode("utf-8"))
# ob.close()
conn = True
while conn:
    msg = input("Enter msg here: ")
    if msg == "no":
        ob.send(msg.encode("utf-8"))
        conn = False
        ob.close()
    else:
        ob.send(msg.encode("utf-8"))


