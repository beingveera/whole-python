from tkinter import *
from tkinter import messagebox
import calendar

root=Tk()
def fun():
	op=val.get()
	bn=valu.get()
	l=int(op)
	v=int(bn)
	pri=calendar.month(l,v)
	messagebox.showinfo("Calendar",pri)

fr=Frame(root)
fr.pack()

fr1=Frame(root)
fr1.pack(padx=20,pady=20)

fr2=Frame(root)
fr2.pack(padx=20,pady=20)

fr3=Frame(root)
fr3.pack(padx=20,pady=20)


lab=Label(fr,text="GUI Calendar",bg="cyan",fg="red", width=40)
lab.pack()


val=StringVar()
valu=StringVar()

lt=Label(fr1,text="Year",fg="blue")
lt.grid()

lk=Entry(fr1,width=10,bd=7, textvariable=val,bg="pink",fg="red")
lk.grid()


ut=Label(fr2,text="Month",fg="blue")
ut.grid()

bk=Entry(fr2,width=10,bd=7, textvariable=valu,bg="pink",fg="red")
bk.grid()



butt=Button(fr3,text="Submit",bd=5,fg="red",bg="yellow", command=fun)
butt.grid()

root.mainloop()