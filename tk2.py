from tkinter import *
master=Tk(className="Registration Details")
#master.geometry("500x500")
var=IntVar()
lb=Label(master,text="Student Admission")

lb1=Label(master,text="Roll No:").grid(row=0)
el=Entry(master).grid(row=0,column=1)

lb2=Label(master,text="First Name:").grid(row=1)
el2=Entry(master).grid(row=1,column=1)

lb3=Label(master,text="Middle Name:").grid(row=2)
el3=Entry(master).grid(row=2,column=1)

lb4=Label(master,text="Last Name:").grid(row=3)
el4=Entry(master).grid(row=3,column=1)

lb5=Label(master,text="Gender:").grid(row=4)
r=Radiobutton(master,text="Male",variable=var,value=1).grid(row=4,column=1)
r1=Radiobutton(master,text="Female",variable=var,value=2).grid(row=4,column=2)

lb5=Label(master,text="Religion:")
lb5.grid(row=5)
Lb6 = Listbox(master,selectmode=SINGLE)
Lb6.grid(row=5,column=1)
Lb6.insert(1,"Hindu")
Lb6.insert(2,"Christian")
Lb6.insert(3,"Muslim")
Lb6.insert(4,"Others")

lb7=Label(master,text="Nationality:").grid(row=6)
el7=Entry(master).grid(row=6,column=1)

lb8=Label(master,text="Select blood group:")
lb8.grid(row=7)

Lb9 = Listbox(master,selectmode=SINGLE)
Lb9.grid(row=8,column=1)
Lb9.insert(1, "A+")
Lb9.insert(2, "A-")
Lb9.insert(3, "B+")
Lb9.insert(4, "B-")
Lb9.insert(3, "o+")
Lb9.insert(4, "o-")

lb10=Label(master,text="Mobile:").grid(row=9)
el10=Entry(master).grid(row=9,column=1)

lb11=Label(master,text="Email:").grid(row=10)
el11=Entry(master).grid(row=10,column=1)

b1=Button(master,text="Submit").grid(row=11,column=0)
b2=Button(master,text="Next").grid(row=11,column=1)





#bt=Button(master,text="submit").grid(row=2,column=1)
master.mainloop()
