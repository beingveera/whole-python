from tkinter import *
import wikipedia as wiki

root=Tk()

do=Label(root,bg="pink",height=30, width= 40)
do.place(x=0,y=40)

bn=Label(root,text="Search",bg="pink",fg="blue")
bn.place(x=33,y=75)

val=StringVar()
def call():
	v1=val.get()
	try:
		data=wiki.summary(v1)
		ar.insert(END,data)
		ar.insert(END,"\n")
		ar.insert(END,"================================================")
	except:
		ar.insert(END,"\n")
		ar.insert(END,"       Invalid Data Entry...!!!!!!")
	
		
	

l=Label(root,text="Wikipedia loader" ,bg="yellow",fg="blue", height=2)
l.pack(fill="x")

e=Entry(root,bg="gold",fg="red",bd=6, textvariable= val)
e.place(x=140,y=70)

ar=Text(root,bg="white",fg="black",font =("Courier", 5),height=32,width=48)
ar.place(x=0,y=120)


but=Button(root,text="Submit",bd=5,bg="cyan",fg='red', command=call)

but.place(x=80,y=750)

but=Button(root,text="Exit",bd=5,bg="cyan",fg='red', command=root.quit)

but.place(x=300,y=750)


root.mainloop()