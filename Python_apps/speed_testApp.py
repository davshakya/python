from tkinter import *
import speedtest


def speed_test():
    sp1 = speedtest.Speedtest()
    sp1.get_servers()
    down = str(round(sp1.download() / (10 ** 6), 3)) + "Mbps"
    up = str(round(sp1.download() / (10 ** 6), 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x500")
sp.config(bg="Blue")
lab = Label(sp, text="Internet Speed Test", font=("time new roman", 20, "bold"))
lab.place(x=120, y=20)

lab = Label(sp, text="Download Speed", font=("time new roman", 20, "bold"))
lab.place(x=120, y=100)
lab_down = Label(sp, text="00", font=("time new roman", 20, "bold"), command=speed_test())
lab_down.place(x=120, y=140)

lab = Label(sp, text="Upload Speed", font=("time new roman", 20, "bold"))
lab.place(x=120, y=200)
lab_up = Label(sp, text="00", font=("time new roman", 20, "bold"))
lab_up.place(x=120, y=240)

button = Button(sp, text="Run Speed Test", font=("time new roman", 20, "bold"), bg="Red", command=speed_test)
button.place(x=120, y=300)
sp.mainloop()
