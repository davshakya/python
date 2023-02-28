from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import pytube
from tkinter import messagebox

root = Tk()
root.title("Lalita Youtube Downloader")
root.geometry("600x400")

def retrieve_input():
    try:
        link=textBox.get("1.0","end-1c")
        print(link)
        ytube = pytube.YouTube(link)
        choice=v.get()
        if choice == 0:
            res="360p"
            ytube.streams.get_by_resolution(res).download()
        if choice == 1:
            res="480p"
            ytube.streams.get_by_resolution(res).download()
        if choice == 2:
            res="720p"
            ytube.streams.get_by_resolution(res).download()
        if choice == 3:
            res="1080p"
            ytube.streams.get_by_resolution(res).download()      
        messagebox.showerror("showerror","Hey! Your video has been doanloaded successfully.\n Thank you for using this application.")
    except:
        messagebox.showerror("showerror", "Try Again! \n There is something wrong with your video link or try with other resolution.")

def close():
   #win.destroy()
   root.quit()       
   
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='More about Lalita Enterprises')
v = IntVar()
inuttext=Label(root, text='Enter the URL of your youtube video link in text box :\n', padx=2).pack(anchor=W)
textBox=Text(root, height=1, width=60,relief='solid', background="yellow")
textBox.pack()
inuttext=Label(root, text='\n Please select resolution from below:', padx=1).pack(anchor=W)

v = IntVar()
rb1=Radiobutton(root, text='360p', variable=v, value=0).pack(anchor=W)
rb2=Radiobutton(root, text='480p', variable=v, value=1).pack(anchor=W)
rb3=Radiobutton(root, text='720p HD', variable=v, value=2).pack(anchor=W)
rb4=Radiobutton(root, text='1080p Full HD', variable=v, value=3).pack(anchor=W)
pb = ttk.Progressbar(root, orient="horizontal", length=600, mode="determinate").pack(anchor=W,padx=7,pady=7)
Button(root,text="Download",font=("Calibri",12,"bold"),bd=5,command=retrieve_input,relief=GROOVE,justify=LEFT).pack(side=LEFT,padx=150)
Button(root, text= "Close", font=("Calibri",12,"bold"),bd=5,relief=GROOVE, command=close).pack(side=LEFT)
root.mainloop()