from tkinter import *
master=Tk(className="log in")
def click():
    lb=Label(master,text="clicked").pack()
bt=Button(master,text="click",command=click).pack()
master.mainloop()
