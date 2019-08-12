import tkinter as tk

root = tk.Tk()

def donothing():
    print("doing nothing")


menu = tk.Menu(root)
root.config(menu=menu)

subMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="new project", command=donothing)
subMenu.add_command(label="one project", command=donothing)
subMenu.add_separator()
subMenu.add_command(label="separator here", command=donothing)
subMenu.add_command(label="Exit", command=donothing)

editMenu = tk.Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="undo", command=donothing)

root.mainloop()