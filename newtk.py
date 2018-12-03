from tkinter import *
master=Tk(className="settings")
#master.geometry("500x500")
lb=Label(master,text="sound",fg="red",bg="green",bd=10,relief=SUNKEN).pack(side=LEFT)
bt=Button(master,text="click here").pack()
el=Entry(master).pack()
master.mainloop()
