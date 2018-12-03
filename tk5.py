from tkinter import *
master=Tk()
can=Canvas(master,width=500,height=500)
can.pack()
can.create_line(50,10,80,40,fill="red")
can.create_line(80,40,50,70,fill="green")
can.create_line(50,70,20,40,fill="blue")
can.create_line(20,40,50,10,fill="red")

master.mainloop()
