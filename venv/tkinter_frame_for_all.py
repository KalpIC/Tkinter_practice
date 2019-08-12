from tkinter import *
from tkinter import messagebox

root = Tk()

def donothing():
    print("doing nothing")

#-------------------Main Menu-------------------#

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="new project", command=donothing)
subMenu.add_command(label="one project", command=donothing)
subMenu.add_separator()
subMenu.add_command(label="separator here", command=donothing)
subMenu.add_command(label="Exit", command=donothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="undo", command=donothing)

#--------------------Toolbar--------------------#

toolbar = Frame(root, bg="blue")

insertBnt = Button(toolbar, text="Insert Image", command=donothing)
insertBnt.pack(side="left", padx=2, pady=2)
printBtn = Button(toolbar, text="Print", command=donothing)
printBtn.pack(side="left", padx=2, pady=2)

toolbar.pack(side="top", fill="x")

#--------------------StatusBar--------------------#

status = Label(root, text="Preparing to do nothing", bd="1", relief="sunken", anchor="w")
status.pack(side="bottom", fill="x")

#-------------------Message Box-------------------#


messagebox.showinfo('Windows Title', 'I don\'t have any fun fact...!')

answer = messagebox.askquestion('First Question', 'Click anything Yes OR No ?')

if answer == 'yes':
    print("YES")
if answer == 'no':
    print("NO")



root.mainloop()
