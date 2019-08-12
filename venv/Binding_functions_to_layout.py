import tkinter as tk

root = tk.Tk()


def printname():
    print("You have just clicked that button  !!!")


btn1 = tk.Button(root, text="This is Button", command=printname)
btn1.pack()

root.mainloop()