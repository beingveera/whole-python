from tkinter import *
from tkinter import messagebox

import instaloader as inl

loader=inl.Instaloader()


root=Tk()

user=StringVar()

def insta():
	name=user.get()
	loader.download_profile(name,profile_pic_only=True)
	messagebox.showinfo("Complete"," Image has been downloaded ")
	
l1=Label(root,text="Instagram Profile Downloader ",bg="cyan",fg="red",height=2)
l1.pack(fill="x")

l2=Label(root,bg="gold", height= 30, width= 100)
l2.pack()

l3=Label(root,text="Username",bg="gold",fg="blue")
l3.place(x=10,y=105)

e1=Entry(root,bd=9,bg="pink",fg="red", textvariable=user)
e1.place(x=140,y=100)

but=Button(root,text="Submit",bd=5,bg="violet", command=insta)

but.place(x=80,y=300)

but1=Button(root,text="Exit",bd=5,bg="violet", command=root.quit)

but.place(x=80,y=300)
but1.place(x=300,y=300)

root.mainloop()