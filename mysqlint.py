from tkinter import *
import mysql.connector

master=Tk(className="Registration Details")
master.geometry("250x200")
master.configure(bg="pink")
master.wm_iconbitmap('s2.ico')

lb=Label(master,text="LOGIN",font = "Times 15 bold underline",bg="pink").grid(row=0,column=1)


lb2=Label(master,text="Username:",bg="pink").grid(row=2,pady=10)
e2=Entry(master)
e2.grid(row=2,column=1,sticky=W)

lb3=Label(master,text="Password:",bg="pink").grid(row=3,pady=10)
e3=Entry(master,show="*")
e3.grid(row=3,column=1,sticky=W)


def submit():
    db = mysql.connector.connect(host="localhost",user="root",password="",database="tkinter")#connector object creation
    cur=db.cursor()

    add_reg=("insert into sign(user_name,passwrd)values(%s,%s)") #%s is also used for integer values
    
    data_reg=(e2.get(),e3.get())
    cur.execute(add_reg,data_reg)
    
    db.commit() #connector object.commit
    db.close()

def read():
    db = mysql.connector.connect(host="localhost",user="root",password="",database="tkinter")#connector object creation
    cur=db.cursor()

    cur.execute("select * from sign;")
    row=cur.fetchall()
    for rows in row:
        print(rows[0],rows[1])
    db.close()







b1=Button(master,text="Submit",command=submit).grid(row=5,column=1,sticky=W)
b2=Button(master,text="Read",command=read).grid(row=5,column=1,sticky=E)

master.mainloop()
