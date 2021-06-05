from tkinter import *
from tkinter import colorchooser
root=Tk()



def run():
	print('techno')
a=Radiobutton(root,text="St",bg="red",highlightbackground="yellow",relief='solid')
b=Radiobutton(root,text="Sc",bg="yellow",highlightbackground="red",relief='groove')
c=Radiobutton(root,text="Gen",bg="cyan",bd=10,highlightcolor="red",relief='raised')
d=Radiobutton(root,text="min",bg="pink",width=10,relief='ridge')
e=Radiobutton(root,text="other",bg="green",fg="purple", relief='sunken')
f=Radiobutton(root,text="Sharma",bg="gray",fg="orange",bd=5,height=2,relief='raised', command=run)
a.pack(padx=20,pady=20,fill="x")
b.pack(padx=20,pady=20,fill="y")
c.pack(padx=20,pady=20,anchor='ne')
d.pack(padx=20,pady=20, anchor="se")
e.pack(padx=20,pady=20, anchor="s")
f.pack(padx=20,pady=20,fill="both")

root.mainloop()