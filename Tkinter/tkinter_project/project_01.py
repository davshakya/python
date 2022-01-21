import tkinter as tk
r=tk.Tk()
r.title("Hello")
button=tk.Button(r,text="Stop",width=50,command=r.destroy)
greeting = tk.Label(text="Hello, Tkinter",foreground="white",background="blue")
entry=tk.Entry()
text=tk.Text()
greeting.pack()
button.pack()
entry.pack()
text.pack()
r.mainloop()






