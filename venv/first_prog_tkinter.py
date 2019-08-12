import tkinter as tk

root = tk.Tk()

thelabel = tk.Label(root, text="Tkinter window First GUI box")
thelabel.pack()

topframe = tk.Frame(root)
topframe.pack()

bottomframe = tk.Frame(root)
bottomframe.pack(side="bottom")

btn1 = tk.Button(topframe, text="Button 1", fg="red")
btn2 = tk.Button(topframe, text="Button 2", fg="blue")
btn3 = tk.Button(topframe, text="Button 3", fg="green")
btn4 = tk.Button(bottomframe, text="Button 4", fg="yellow")

btn1.pack(side="left")
btn2.pack(side="left")
btn3.pack(side="left")
btn4.pack()




root.mainloop()
