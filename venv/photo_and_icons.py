from tkinter import *

root = Tk()

photo = PhotoImage(file="python_icon.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()