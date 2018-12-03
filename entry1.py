from tkinter import *
master=Tk(className="Login form")
master.geometry("200x200")
master.configure(bg="light blue")

lb=Label(master,text="Username:",bg="light blue")
lb.grid(row=1,pady=5)
e=Entry(master)
e.grid(row=1,column=1,sticky=W)

def clicked():
    print(e.get())

b1=Button(master,text="Login",command=clicked)
b1.grid(row=3)

master.mainloop()
