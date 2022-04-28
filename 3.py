from tkinter import *

root = Tk()

Console = Text(root)
Console.pack()

root.mainloop()



def write(*message, end = "\n", sep = " "):
    text = ""
    for item in message:
        text += "{}".format(item)
        text += sep
    text += end
    Console.insert(INSERT, text)
