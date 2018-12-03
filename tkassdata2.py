from tkinter import *
import mysql.connector

master=Tk(className="Registration Details")
master.geometry("400x650")
master.configure(bg="pink")
master.wm_iconbitmap('s2.ico')

lb=Label(master,text="Student Admission",font = "Times 15 bold underline",bg="pink").grid(row=0,column=1)


lb2=Label(master,text="First Name:",bg="pink").grid(row=2,pady=10)
e2=Entry(master)
e2.grid(row=2,column=1,sticky=W)

lb3=Label(master,text="Middle Name:",bg="pink").grid(row=3,pady=10)
e3=Entry(master)
e3.grid(row=3,column=1,sticky=W)

lb4=Label(master,text="Last Name:",bg="pink").grid(row=4)
e4=Entry(master)
e4.grid(row=4,column=1,sticky=W)



def submit():
    db = mysql.connector.connect(host="localhost",user="root",password="",database="tkinter")#connector object creation
    cur=db.cursor()

    cur.execute("insert into student(First_name,Middle_Name,Last_Name) values(e2.get(),e3.get(),e4.get())")
    
    
    db.commit() #connector object.commit
    db.close()



b1=Button(master,text="Submit",command=submit).grid(row=5,column=1)

master.mainloop()
