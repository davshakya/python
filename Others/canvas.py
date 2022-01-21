from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400
root.title("GUI with Dev")
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack() 
can_widget.create_line(0,0, 800,200, fill="red")  
can_widget.create_line(0,400, 800,0, fill="red")  
can_widget.create_rectangle(3,7,700,300, fill="red")
can_widget.create_text(200,200, text="Devendra")
can_widget.create_oval(200,100,20,10 )
root.mainloop()
 
 
