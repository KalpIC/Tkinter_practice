from tkinter import *

root = Tk()
entry_1 = Entry(root).pack()
entry_2 = Entry(root).pack()


def entry():
    entry = getint(entry_1)+ getint(entry_2)

Label(root, text=entry, bg="blue").pack()

root.mainloop()