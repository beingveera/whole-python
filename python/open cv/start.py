from tkinter import * 
from tkinter import messagebox
import cv2



def add():
    y=Tk()

    name=StringVar()
    fname=StringVar()
    mname=StringVar()
    dob=StringVar()
    mail=StringVar()
    mob=StringVar()
    Add=StringVar() 

    y.title("Ragistration")
    y.geometry("400x400")
    l1=Label(y,text="Enter your`s Details ", bg="orange",height=3,width=100,border=3)
    l1.place(x=350,y=10)
    
    l2=Label(y,text="Name :", bg="orange")
    l2.place(x=500,y=100)
    e1=Entry(y,width=45,border=5,textvariable = name)
    e1.place(x=600,y=100)

    l3=Label(y,text="Father`s Name :", bg="orange")
    l3.place(x=500,y=160)
    e2=Entry(y,width=45,border=5,textvariable = fname)
    e2.place(x=600,y=160)

    l4=Label(y,text="Mother`sName :", bg="orange")
    l4.place(x=500,y=220)
    e3=Entry(y,width=45,border=5,textvariable = mname)
    e3.place(x=600,y=220)

    l5=Label(y,text="Date of Birth :", bg="orange")
    l5.place(x=500,y=280)
    e4=Entry(y,width=45,border=5,textvariable =dob)
    e4.place(x=600,y=280)

    l6=Label(y,text="Email :", bg="orange")
    l6.place(x=500,y=340)
    e5=Entry(y,width=45,border=5,textvariable = mail)
    e5.place(x=600,y=340)

    l7=Label(y,text="Mobile No :", bg="orange")
    l7.place(x=500,y=400)
    e6=Entry(y,width=45,border=5,textvariable = mob)
    e6.place(x=600,y=400)

    l8=Label(y,text="Address :", bg="orange")
    l8.place(x=500,y=460)
    e7=Entry(y,width=45,border=5,textvariable=Add)
    e7.place(x=600,y=460)

  
    pm=name.get()
    print(pm)
    def Submit():
        km=name.get()
        print(km)

       
        with open("{}.txt".format(km),"a+") as op:
            op.write(km)

        messagebox.showinfo("Complete","Data is Submitted...!!!")




    s1=Button(y,text="Submit",border=4,width=10,bg="skyblue",command=Submit)
    s2=Button(y,text="Cancel",border=4,width=10,bg="skyblue",command=quit)
    s1.place(x=630,y=550)
    s2.place(x=750,y=550)

    


    y.mainloop()


def ward1():
    a=Tk()
    a.title("WARD 1 ")
    a.geometry("400x200")
    b=Frame(a,bg="gray",height=50,width=500)
    b.pack()
    v=Label(a,text="Enter your Id :- ")
    c=Entry(a,border=3)
    s=Button(a,text="Submit",command=entry)
    s.place(x=150,y=145)
    p=Button(a,text="Cancel")
    p.place(x=220,y=145)
    v.place(x=60,y=90)
    c.place(x=150,y=90)

    a.mainloop()

def ward2():
    a=Tk()
    a.title("WARD 2 ")
    a.geometry("400x400")
    a.mainloop()

def ward3():
    a=Tk()
    a.title("WARD 3 ")
    a.geometry("400x400")
    a.mainloop()

def ward4():
    a=Tk()
    a.title("WARD 4 ")
    a.geometry("400x400")
    a.mainloop()

def ward5():
    a=Tk()
    a.title("WARD 5 ")
    a.geometry("400x400")
    a.mainloop()

def ward6():
    a=Tk()
    a.title("WARD 6 ")
    a.geometry("400x400")
    a.mainloop()

def ward7():
    a=Tk()
    a.title("WARD 7 ")
    a.geometry("400x400")
    a.mainloop()

def ward8():
    a=Tk()
    a.title("WARD 8 ")
    a.geometry("400x400")
    a.mainloop()

def ward9():
    a=Tk()
    a.title("WARD 9 ")
    a.geometry("400x400")
    a.mainloop()

def ward10():
    a=Tk()
    a.title("WARD 10 ")
    a.geometry("400x400")
    a.mainloop()

def ward11():
    a=Tk()
    a.title("WARD 11 ")
    a.geometry("400x400")
    a.mainloop()

def ward12():
    a=Tk()
    a.title("WARD 12 ")
    a.geometry("400x400")
    a.mainloop()


def entry():
    z=Tk()
    z.title(pm)
    z.geometry("400x400")
    z.mainloop()



























































x=Tk()
x.title("Smart IV")
x.geometry("1350x1000")

f1=Frame(x,background="white",height=50,width=1000)
l1=Label(f1,text="SMART IV STAND",background="white",foreground="red",width=100,height=3)
l1.pack()
f1.pack()

f2=Frame(x,background="pink",height=300,width=300)
f2.place(x=30,y=100)
f4=Frame(x,background="pink",height=300,width=300)
f4.place(x=370,y=100)
f3=Frame(x,background="pink",height=300,width=300)
f3.place(x=710,y=100)
f5=Frame(x,background="pink",height=300,width=300)
f5.place(x=1045,y=100)



l1=Label(f2,text="REGISTRATION SECTION",height=2,background="black",foreground="red",width=40)
l1.place(x=8,y=10)

b1=Button(f2,text="Add Patient",bg="yellow",command=add,width=10)
b1.place(x=10,y=70)

b2=Button(f2,text="Decices",bg="yellow",width=10)
b2.place(x=110,y=70)

b3=Button(f2,text="Allaotment",bg="yellow",width=10)
b3.place(x=210,y=70)

b4=Button(f2,text="Patient List",bg="yellow",command=add,width=10)
b4.place(x=10,y=120)

b5=Button(f2,text="Update ",bg="yellow",width=10)
b5.place(x=110,y=120)

b6=Button(f2,text="Delete ",bg="yellow",width=10)
b6.place(x=210,y=120)




l1=Label(f4,text="HOSPITAL WARDS",height=2,background="black",foreground="red",width=40)
l1.place(x=8,y=10)


b1=Button(f4,text="Ward 1.",bg="yellow",command=ward1)
b1.place(x=10,y=70)

b2=Button(f4,text="Ward 2.",bg="yellow",command=ward2)
b2.place(x=80,y=70)

b3=Button(f4,text="Ward 3.",bg="yellow",command=ward3)
b3.place(x=150,y=70)

b4=Button(f4,text="Ward 4.",bg="yellow",command=ward4)
b4.place(x=220,y=70)


b5=Button(f4,text="Ward 5.",bg="yellow",command=ward5)
b5.place(x=10,y=120)

b6=Button(f4,text="Ward 6.",bg="yellow",command=ward6)
b6.place(x=80,y=120)

b7=Button(f4,text="Ward 7.",bg="yellow",command=ward7)
b7.place(x=150,y=120)

b8=Button(f4,text="Ward 8.",bg="yellow",command=ward8)
b8.place(x=220,y=120)


b9=Button(f4,text="Ward 9.",bg="yellow",command=ward9)
b9.place(x=10,y=170)

b10=Button(f4,text="Ward 10.",bg="yellow",command=ward10)
b10.place(x=80,y=170)

b11=Button(f4,text="Ward 11.",bg="yellow",command=ward11)
b11.place(x=150,y=170)

b12=Button(f4,text="Ward 12.",bg="yellow",command=ward12)
b12.place(x=220,y=170)









mainloop()