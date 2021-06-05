from tkinter import * 
from tkinter import messagebox
import smtplib as s



def Submit():
    da=b.get()
    dz=k.get()
    db=c.get()
    dc=d.get()
    dd=e.get()
    de=f.get()
    df=g.get()
    dg=h.get()
    with open("{}.txt".format(da),"a+") as dp:
        dp.write("{} \t {} \t {} \t {} \t {} \t {} \t {} \t \t \n\n".format(da,dz,db,dc,dd,de,df,dg))
    
    messagebox.showinfo("Complete","Data is Submitted")

a=Tk()
a.geometry("400x500")
a.title("Ragistration")

fr=Frame(a,bg="gray",height=30,width=400)
fr.pack()

b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()
h=StringVar()
k=StringVar()

p=Entry(a,textvariable=b,border=4)
p.place(x=170,y=50)
pl=Entry(a,textvariable=k,border=4)
pl.place(x=170,y=100)
q=Entry(a,textvariable=c,border=4)
q.place(x=170,y=150)
r=Entry(a,textvariable=d,border=4)
r.place(x=170,y=200)
s=Entry(a,textvariable=e,border=4)
s.place(x=170,y=250)
t=Entry(a,textvariable=f,border=4)
t.place(x=170,y=300)
u=Entry(a,textvariable=g,border=4)
u.place(x=170,y=350)
v=Entry(a,textvariable=h,border=4)
v.place(x=170,y=400)



l9=Label(a,text="First Name",bg="yellow")
l9.place(x=30,y=50)

l10=Label(a,text="Last Name",bg="yellow")
l10.place(x=30,y=100)

l2=Label(a,text="Father`s Name",bg="yellow")
l2.place(x=30,y=150)

l3=Label(a,text="Mother`s Name",bg="yellow")
l3.place(x=30,y=200)

l4=Label(a,text="Dob",bg="yellow")
l4.place(x=30,y=250)

l5=Label(a,text="Email",bg="yellow")
l5.place(x=30,y=300)

l6=Label(a,text="Mobile No.",bg="yellow")
l6.place(x=30,y=350)

l7=Label(a,text="Address",bg="yellow")
l7.place(x=30,y=400)

asd=Button(a,text="Submit",command=Submit)
asd.place(x=140,y=450)

asf=Button(a,text="Cancel",command=quit)
asf.place(x=240,y=450)

a.mainloop()