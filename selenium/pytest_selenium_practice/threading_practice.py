import threading
from threading import Thread
t=threading.current_thread().getName()
print(t)


def disp():
    print("Chiled running")
t=Thread(target=disp)
t.start()

# def disp(a,b):
#     print("Thread running", a,b)
# t=Thread(target=disp,args=(10,20))
# t.start()

#
#
# def disp(a,b):
#     print("Thread running", a,b)
# for i in range(5):
#     t=Thread(target=disp,args=(10,20))
#     t.start()