from tkinter import *
import tkinter.messagebox as tkMessageBox

root = Tk()
def Exit():
    result = tkMessageBox.askquestion('Python: Simple CRUD Applition', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

label_1 = Label(root, text="Username")
label_2 = Label(root, text="Password")

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
   

checkbox = Checkbutton(root, text="Keep me logged in")
checkbox.grid(columnspan=2)

btn_exit = Button(root, width=10, text="Exit", command=Exit)
btn_exit.grid(column=0, row=4)


root.mainloop()
