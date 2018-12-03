from tkinter import *
import tkinter #import tkinter module
window=tkinter.Tk() #create a new window
window.title("Sign in") #window title
window.geometry("300x800") #window size
window.wm_iconbitmap('s2.ico') #adding icon to the window

lbl=tkinter.Label(window,text="username",fg="Navy") #create a label widget called 'Label', arguments show that inside 'window' and text.
lbl.pack() #which put label inside window

ent=tkinter.Entry(window)
ent.pack() #put entry inside window


lbe=tkinter.Label(window,text="password",fg="Navy")
lbe.pack()

ent1=tkinter.Entry(window) #create an entry
ent1.pack()

btn=tkinter.Button(window,text="click",bg="white") #create button
btn.pack() #put button inside window

#photo= tkinter.PhotoImage(file="vivian.pgm")
#pic=tkinter.Label(window,image=photo)
#pic.pack()

#CheckVar1 = IntVar()
#CheckVar2 = IntVar()

C1 = tkinter.Checkbutton(window, text = "Music", variable =IntVar,onvalue = 1, offvalue = 0, height=5,width = 20) #creating check button
C1.pack()
C2 = tkinter.Checkbutton(window, text = "Video", variable =IntVar,onvalue = 1, offvalue = 0, height=5,width = 20) 
C2.pack()


#listbox creation
Lb1 = Listbox(window,selectmode=MULTIPLE)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()
btn1=tkinter.Button(window,text="Submit",bg="white") #create button
btn1.pack() #put button inside window


#menu creation
mb =tkinter.Menubutton ( window, text = "options") #menu button options creation
mb.pack()

mb.menu  =  Menu (mb,tearoff=0)
mb["menu"]  =  mb.menu

mb.menu.add_checkbutton ( label = "option 1",variable =IntVar)
mb.menu.add_checkbutton ( label = "option 2",variable =IntVar)

mb.pack()



#panedwindow
pw = PanedWindow(window,orient=VERTICAL)
pw.pack()
#pw.pack(fill=BOTH, expand=1)

top = Label(pw, text="top pane")
pw.add(top)

bottom = Label(pw, text="bottom pane")
pw.add(bottom)








window.mainloop()
