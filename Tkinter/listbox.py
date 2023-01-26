import pygame
from pygame import mixer
from tkinter import *
import os
from PIL import Image, ImageTk

root = Tk()

Lb1 = Listbox(root, height = 10,  
                  width = 15,  
                  bg = "grey", 
                  activestyle = 'dotbox',  
                  font = "Helvetica", 
                  fg = "yellow",
                  highlightcolor='yellow',
                  highlightthickness=5) 
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()
root.mainloop()
