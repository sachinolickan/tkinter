from tkinter import *
import tkinter.messagebox as tkMessageBox
from tkinter.scrolledtext import ScrolledText


master=Tk(className="Registration Details")
master.geometry("400x650")
master.configure(bg="pink")
master.wm_iconbitmap('s2.ico')

var=IntVar()
lb=Label(master,text="Student Admission",font = "Times 15 bold underline",bg="pink").grid(row=0,column=1)

img=PhotoImage(file="profile.png")
Lab=Label(master,image=img)
Lab.grid(row=2,column=3)



lb1=Label(master,text="Roll No:",bg="pink").grid(row=1)
el=Entry(master).grid(row=1,column=1,sticky=W)

lb2=Label(master,text="First Name:",bg="pink").grid(row=2)
el2=Entry(master).grid(row=2,column=1,sticky=W)

lb3=Label(master,text="Middle Name:",bg="pink").grid(row=3,pady=10)
el3=Entry(master).grid(row=3,column=1,sticky=W)

lb4=Label(master,text="Last Name:",bg="pink").grid(row=4)
el4=Entry(master).grid(row=4,column=1,sticky=W)

lb5=Label(master,text="Gender:",bg="pink").grid(row=5)
r=Radiobutton(master,text="Male",variable=var,value=1,bg="pink").grid(row=5,column=1,sticky=W)
r1=Radiobutton(master,text="Female",variable=var,value=2,bg="pink").grid(row=6,column=1,sticky=W)



lb5=Label(master,text="Religion:",bg="pink")
lb5.grid(row=7,pady=10)
variable = StringVar(master)
variable.set("choose religion") # default value
option = OptionMenu(master, variable, "Hindu", "Christian", "Muslim","others")
option.grid(row=7,column=1,sticky=W)













'''Lb6 = Listbox(master,selectmode=SINGLE)
Lb6.grid(row=7,column=1)
Lb6.insert(1,"Hindu")
Lb6.insert(2,"Christian")
Lb6.insert(3,"Muslim")
Lb6.insert(4,"Others")'''

lb7=Label(master,text="Nationality:",bg="pink").grid(row=8,pady=10)
el7=Entry(master).grid(row=8,column=1,sticky=W)

lb8=Label(master,text="blood group:",bg="pink")
lb8.grid(row=9)
vari = StringVar(master)
vari.set("blood group") # default value
option = OptionMenu(master, vari, "O+", "O-", "A+","A-","B+","B-")
option.grid(row=9,column=1,sticky=W)


'''Lb9 = Listbox(master,selectmode=SINGLE)
Lb9.grid(row=9,column=1)
Lb9.insert(1, "A+")
Lb9.insert(2, "A-")
Lb9.insert(3, "B+")
Lb9.insert(4, "B-")
Lb9.insert(3, "o+")
Lb9.insert(4, "o-")'''

lb10=Label(master,text="Mobile:",bg="pink").grid(row=10,pady=10)
el10=Entry(master).grid(row=10,column=1,sticky=W)

lb11=Label(master,text="Email:",bg="pink").grid(row=11,pady=10)
el11=Entry(master).grid(row=11,column=1,sticky=W)


#box
lb12=Label(master,text="Address:",bg="pink").grid(row=12,padx=30)
ScrolledText(master,height=7,width=20).grid(row=12,column=1,sticky=W,pady=10)



#dialoguebox

def Exit():
    result = tkMessageBox.askquestion('Python: Simple CRUD Applition', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        master.destroy()
        exit()

b1=Button(master,text="Submit").grid(row=13,column=1)
b2=Button(master,text="Exit",command=Exit).grid(row=13,column=2,sticky=E)



#bt=Button(master,text="submit").grid(row=2,column=1)
master.mainloop()
