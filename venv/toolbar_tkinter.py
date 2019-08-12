from tkinter import *


root = Tk()

def donothing():
    print("Doing Nothing")

toolbar = Frame(root, bg="blue")

insertBnt = Button(toolbar, text="Insert Image", command=donothing)
insertBnt.pack(side="left", padx=2, pady=2)
printBtn = Button(toolbar, text="Print", command=donothing)
printBtn.pack(side="left", padx=2, pady=2)


toolbar.pack(side="top", fill="x")

root.mainloop()