import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()
def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()
def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()
def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()    
root=Tk()
root.title('e-Lalita Music Player')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")
playlist=Listbox(root,selectmode=SINGLE,bg="Gray",fg="Yellow",font=('Ariel',15),width=40,highlightthickness=15,highlightcolor='yellow',)
playlist.grid(columnspan=5)
os.chdir(r'C:\Users\davsh\Music')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)
playbtn=Button(root,text="Play",command=playsong,bd=5,activeforeground="blue",relief=GROOVE)
playbtn.config(font=('cooper',20),bg="green",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)
pausebtn=Button(root,text="Pause",command=pausesong,bd=5,relief=GROOVE)
pausebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)
stopbtn=Button(root,text="Stop",command=stopsong,bd=5,relief=GROOVE)
stopbtn.config(font=('arial',20),bg="red",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)
Resumebtn=Button(root,text="Resume",command=resumesong,bd=5,relief=GROOVE)
Resumebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3) 
mainloop()


 