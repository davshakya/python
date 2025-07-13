from tkinter import *
from tkinter import filedialog, messagebox, font

# Setup main window
root = Tk()
root.title("Lalita Notepad")
root.geometry("800x600")
root.iconbitmap(None)

# Global variables
file_path = None

# Text editor widget
text_area = Text(root, undo=True, wrap='word', font=("Consolas", 12))
text_area.pack(expand=True, fill='both')

# Scrollbar
scroll = Scrollbar(text_area)
scroll.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll.set)
scroll.config(command=text_area.yview)

# ----- File operations -----
def new_file():
    global file_path
    file_path = None
    text_area.delete(1.0, END)
    root.title("Untitled - Notepad")

def open_file():
    global file_path
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if path:
        file_path = path
        with open(path, "r", encoding="utf-8") as f:
            text_area.delete(1.0, END)
            text_area.insert(END, f.read())
        root.title(f"{file_path} - Notepad")

def save_file():
    global file_path
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, END))
        messagebox.showinfo("Saved", "File saved successfully!")
    else:
        save_as()

def save_as():
    global file_path
    path = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if path:
        file_path = path
        with open(path, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, END))
        root.title(f"{file_path} - Notepad")
        messagebox.showinfo("Saved", "File saved successfully!")

# ----- Edit operations -----
def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def undo():
    text_area.event_generate("<<Undo>>")

def redo():
    text_area.event_generate("<<Redo>>")

# ----- Font selection -----
def choose_font():
    font_name = font_var.get()
    size = size_var.get()
    text_area.config(font=(font_name, size))

# ----- Menu -----
menu_bar = Menu(root)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As...", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Font menu
font_menu = Menu(menu_bar, tearoff=0)
font_var = StringVar(value="Consolas")
size_var = IntVar(value=12)

font_list = ["Consolas", "Arial", "Courier", "Helvetica", "Times New Roman"]
for font_name in font_list:
    font_menu.add_radiobutton(label=font_name, variable=font_var, value=font_name, command=choose_font)

size_menu = Menu(font_menu, tearoff=0)
for s in range(8, 33, 2):
    size_menu.add_radiobutton(label=str(s), variable=size_var, value=s, command=choose_font)

font_menu.add_cascade(label="Font Size", menu=size_menu)
menu_bar.add_cascade(label="Font", menu=font_menu)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Lalita Notepad\nBy Devendra"))
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()
