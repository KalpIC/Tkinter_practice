import tkinter as tk


class firstbutton:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.printbutton = tk.Button(frame, text="Print my message", command=self.printmessage)
        self.printbutton.pack(side="left")

        self.quitbutton = tk.Button(frame, text="Quit", command=frame.quit)
        self.quitbutton.pack(side="left")

    def printmessage(self):
            print("your button is working.......!!!!")


root = tk.Tk()

b = firstbutton(root)

root.mainloop()