from tkinter import *
import tkinter.messagebox as tkMessageBox

master=Tk(className="Login form")
master.geometry("200x200")
master.configure(bg="light blue")
master.wm_iconbitmap('s2.ico')

e1=StringVar()

lb=Label(master,text="LOGIN",font = "Times 15 bold",bg="light blue").grid(row=0,column=1)

lb1=Label(master,text="Username:",bg="light blue")
lb1.grid(row=1,pady=5)
e1=Entry(master)
e1.grid(row=1,column=1,sticky=W)


lb2=Label(master,text="Password:",bg="light blue")
lb2.grid(row=2,pady=10)
e2=Entry(master,show="*")
e2.grid(row=2,column=1,sticky=W)

def clicked():
    print(e1.get())


def Exit():
    result = tkMessageBox.askquestion('Python: Simple CRUD Applition', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        master.destroy()
        exit()
def clicked():
        # print("Clicked")
        username = e1.get()
        password = e2.get()
        if username == "admin" and password == "admin":
            tm.showinfo("Login info", "Welcome Admin")
        else:
            tm.showerror("Login error", "Incorrect username")


        
b1=Button(master,text="Login",command=clicked).grid(row=3)
b2=Button(master,text="Exit",command=Exit).grid(row=3,column=1)


master.mainloop()
