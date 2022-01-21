from tkinter import*
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad by Elalita")
    file=None
    TextArea.delete(1.0, END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ "- Notepad by Elalita")
        TextArea.delete(1.0, END)
        f=open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close 
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file=="": 
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad by Elalita")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file)+"-Notepad by Elalita")
def cutFile():
    TextArea.event_generate(("<<Cut>>"))
def copyFile():
    TextArea.event_generate(("<<Copy>>"))
def pasteFile(): 
    TextArea.event_generate(("<<Paste>>"))
def errorFile():
    tmsg.showinfo("Error","Please visit on www.elalita.com")
def aboutFile():
    tmsg.showinfo("Notepad by Elalita"," Crafted by Lalita Enterprises \n Lahariyapurwa, Jail Road, Orai, Uttar Pradesh \n India ")
    print("Crafted by Lalita Enterprises")

if __name__=='__main__':
 root=Tk()
 root.iconbitmap('1.ico')
 root.title("Untitled-Notepad by Elalita")
 root.geometry("800x600")
 TextArea=Text(root,font="lucida 13")
 file=None
 TextArea.pack(expand=True, fill=BOTH)

 MenuBar=Menu(root)
 #file menu start
 FileMenu=Menu(MenuBar,tearoff=0)
 FileMenu.add_command(label="New",command=newFile)
 FileMenu.add_command(label="Open",command=openFile)
 FileMenu.add_command(label="Save",command=saveFile)
 FileMenu.add_separator()
 FileMenu.add_command(label="Exit",command=quit)
 MenuBar.add_cascade(label="File",menu=FileMenu)
 #file menu end

 #edit menu start
 EditMenu=Menu(MenuBar,tearoff=0)
 EditMenu.add_command(label="Cut",command=cutFile)
 EditMenu.add_command(label="Copy",command=copyFile)
 EditMenu.add_command(label="Paste",command=pasteFile)
 MenuBar.add_cascade(label="Edit",menu=EditMenu)
 #edit menu end

 #Help menu start
 HelpMenu=Menu(MenuBar,tearoff=0)
 HelpMenu.add_command(label="Error",command=errorFile)
 HelpMenu.add_command(label="About",command=aboutFile)
 MenuBar.add_cascade(label="Help",menu=HelpMenu)
 #Help menu end

 root.config(menu=MenuBar)
 
 #Start Scroll Bar
 Scroll=Scrollbar(TextArea)
 Scroll.pack(side=RIGHT,fill=Y)
 Scroll.config(command=TextArea.yview)
 TextArea.config(yscrollcommand=Scroll.set)
 #End Scroll Bar
 
 root.mainloop()


 













