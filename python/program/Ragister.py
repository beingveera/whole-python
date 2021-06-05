from tkinter import *
from tkinter import messagebox
root=Tk()

val1=StringVar()
val2=StringVar()
val3=StringVar()
val4=StringVar()

col=['black','brown','red','orange','yellow','green','blue','violet','gray','white']

mul=['black','brown','red','orange','yellow','green','blue','violet','gold','silver']

tol=['gold','silver',"none"]



def data():
	v1=val1.get()
	v2=val2.get()
	v3=val3.get()
	v4=val4.get()
	
	if v1 not in col:
		messagebox.showwarning("warning","First Color is Invalid.....")
		
	if v2 not in col:
		messagebox.showwarning("warning","Second Color is Invalid.....")
		
	if v3 not in mul:
		messagebox.showwarning("warning","Third Color is Invalid.....")
		
	if v4 not in tol:
		messagebox.showwarning("warning","Forth Color is Invalid.....")
	
	if v1 == 'black':
		c1=0
	elif v1 == 'brown':
		c1=1
	elif v1 == 'red':
		c1=2		
	elif v1 == 'orange':
		c1=3
	elif v1 == 'yellow':
		c1=4
	elif v1 == 'green':
		c1=5
	elif v1 == 'blue':
		c1=6
	elif v1 == 'violet':
		c1=7
	elif v1 == 'gray':
		c1=8
	elif v1 == 'white':
		c1=9
		
	if v2 == 'black':
		c2=0
	elif v2 == 'brown':
		c2=1
	elif v2 == 'red':
		c2=2		
	elif v2 == 'orange':
		c2=3
	elif v2 == 'yellow':
		c2=4
	elif v2 == 'green':
		c2=5
	elif v2 == 'blue':
		c2=6
	elif v2 == 'violet':
		c2=7
	elif v2 == 'gray':
		c2=8
	elif v2 == 'white':
		c2=9
		
	if v3 == 'black':
		c3="10^0"
	elif v3 == 'brown':
		c3="10^1"
	elif v3 == 'red':
		c3="10^2"		
	elif v3 == 'orange':
		c3="10^3"
	elif v3 == 'yellow':
		c3="10^4"
	elif v3 == 'green':
		c3="10^5"
	elif v3 == 'blue':
		c3="10^6"
	elif v3 == 'gold':
		c3=0.1
	elif v3 == 'silver':
		c3=0.01
	
	if v4 == 'gold':
		c4="+-5%"
	elif v4 == 'silver':
		c4="+-10%"
		
	code=("{}{} x {} Ω  {} tolerance".format(c1,c2,c3,c4))

	messagebox.showinfo("Color Code ",code,bd=5)
			

l1=Label(root,text="Ragister Application ",padx=10,pady=20,bg="red",fg="yellow")
l1.pack(fill="x")

l2=Label(root,text="First :",fg="blue")
l2.place(x=40,y=100)

e1=Entry(root,bg="pink",fg="red",bd=9,textvariable= val1)
e1.place(x=120,y=100)

l3=Label(root,text="Second :",fg="blue")
l3.place(x=5,y=200)

e2=Entry(root,bg="pink",fg="red",bd=9,textvariable= val2)
e2.place(x=120,y=200)

l4=Label(root,text="Third :",fg="blue")
l4.place(x=30,y=300)

e3=Entry(root,bg="pink",fg="red",bd=9,textvariable= val3)
e3.place(x=120,y=300)

l5=Label(root,text="Forth :",fg="blue")
l5.place(x=30,y=400)

e4=Entry(root,bg="pink",fg="red",bd=9,textvariable= val4)
e4.place(x=120,y=400)

butt=Button(root,text="Submit",bd=5,bg="cyan",fg="red", command= data)

butt.place(x=90,y=500)

butt1=Button(root,text="Exit",bd=5,bg="cyan",fg="red", command= root.quit)

butt1.place(x=300,y=500)

la=Label(text=None,bg="red",width=100,height=200)
la.place(x=0,y=580)

root.mainloop()