
from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 1')
def restart_time():
    os.system('shutdown /r /t 20')
def logout():
    os.system('shutdown -l')
def shutdown():
    os.system('shutdown /s /t 1')

st=Tk()
st.title("Shutdown")
st.geometry("500x450")
st.config(bg="Blue")
r_button=Button(st,text="Restart", font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=restart)
r_button.place(x=150,y=50,height=50,width=200)
rt_button=Button(st,text="Restart With Time", font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=restart_time)
rt_button.place(x=150,y=150,height=50,width=300)
lg_button=Button(st,text="Log out", font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=logout)
lg_button.place(x=150,y=250,height=50,width=200)
st_button=Button(st,text="Shutdown", font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=shutdown)
st_button.place(x=150,y=350,height=50,width=200)
st.mainloop()

