#  fitting widgets in Layout
#
#
import tkinter as tk

root = tk.Tk()

one = tk.Label(root, text="One text", bg="red", fg="white")
one.pack()
two = tk.Label(root, text="two text", bg="green", fg="black")
two.pack(fill="x")
three = tk.Label(root, text="three text", bg="blue", fg="white")
three.pack(side="left", fill="y")


root.mainloop()