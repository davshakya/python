from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import pytube
from tkinter import messagebox

class YtubeDownloader():
    def __init__(self):
        self.root = Tk()
        self.root.title("Lalita Youtube Downloader 1.2")
        self.root.geometry("600x400")
        self.bytes = 0
        self.maxbytes = 0
        self.mainApp()
        self.root.mainloop()
    def retrieve_input(self):
        try:
            link=self.textBox.get("1.0","end-1c")
            print(link)
            ytube = pytube.YouTube(link)
            choice=self.v.get()
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
            messagebox.showinfo("Information","Hey! Your video has been doanloaded successfully.\n Thank you for using this application.")
        except:
            messagebox.showerror("Error", "Try Again! \n There is something wrong with your video link or try with other resolution.")

    
    def mainApp(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Exit', command=self.root.quit)
        helpmenu = Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='More about Lalita Enterprises')
        v = IntVar()
        inuttext=Label(self.root, text='Enter the URL of your youtube video link in text box :\n', padx=2).pack(anchor=W)
        textBox=Text(self.root, height=1, width=60,relief='solid', background="yellow")
        textBox.pack()
        inuttext=Label(self.root, text='\n Please select resolution from below:', padx=1).pack(anchor=W)

        v = IntVar()
        rb1=Radiobutton(self.root, text='360p', variable=v, value=0).pack(anchor=W)
        rb2=Radiobutton(self.root, text='480p', variable=v, value=1).pack(anchor=W)
        rb3=Radiobutton(self.root, text='720p HD', variable=v, value=2).pack(anchor=W)
        rb4=Radiobutton(self.root, text='1080p Full HD', variable=v, value=3).pack(anchor=W)

        # pb = ttk.Progressbar(self.root, orient="horizontal", length=600, mode="determinate").pack(anchor=W,padx=7,pady=7)
        self.progress = ttk.Progressbar(self.root, orient="horizontal",length=200, mode="determinate").pack(anchor=W,padx=7,pady=7)
        Button(self.root,text="Download",font=("Calibri",12,"bold"),bd=5,command=self.retrieve_input,relief=GROOVE,justify=LEFT).pack(side=LEFT,padx=150)
        Button(self.root, text= "Close", font=("Calibri",12,"bold"),bd=5,relief=GROOVE, command=self.close).pack(side=LEFT)
    
    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 500
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)
    
    def dwonload(self):
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000
        self.read_bytes()

    
    def close(self):
        self.root.quit()   
        
        

YtubeDownloader()