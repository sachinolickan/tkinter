from tkinter import *
master=Tk(className="log in")
def click():
    print("clicked")
bt=Button(master,text="click",command=click).pack()
master.mainloop()
