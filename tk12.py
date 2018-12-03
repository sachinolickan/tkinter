from tkinter import *
master=Tk()
pw = PanedWindow(master,orient=VERTICAL)
pw.pack()
#m.pack(fill=BOTH, expand=1)

top = Label(pw, text="top pane")
pw.add(top)

bottom = Label(pw, text="bottom pane")
pw.add(bottom)

master.mainloop()
