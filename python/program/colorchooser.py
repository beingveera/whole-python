from tkinter import *
from tkinter import colorchooser
root=Tk()

l=colorchooser.askcolor(color="red",title="colors", parent=root)

print(l)

root.mainloop()