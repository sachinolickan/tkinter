from tkinter import *
master=Tk()
can=Canvas(master,width=400,height=400)
can.pack()
can.create_arc(0,0,330,150,start=0,extent=40)
master.mainloop()
