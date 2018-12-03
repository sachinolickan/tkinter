from tkinter import *
master=Tk()

var=IntVar()

def call():
    print("you selected"+ str(var.get()))

lb=Label(master, text="select option",padx=20).pack(anchor=W)
r=Radiobutton(master,text="Python",variable=var,value=1,command=call).pack(anchor=W)
r1=Radiobutton(master,text="Java",variable=var,value=2,command=call).pack(anchor=W)

               
master.mainloop()
