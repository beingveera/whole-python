from tkinter import *
from tkinter import messagebox

class smart:

    def Submit(self):
        finame=StringVar()
        lname=StringVar()
        fname=StringVar()
        mname=StringVar()
        dob=StringVar()
        mob=IntVar()
        mail=StringVar()
        address=StringVar()




    def ragi(self):
        ra=Tk()
        ra.geometry("400x400")
        ra.title("Ragistration")

        r1=Frame(ra,width=400,height=30,bg="red").pack()

        r2=Frame(ra,width=400,height=370,bg="lightgray").place(x=0,y=30)

        l1=Label(ra,text="First_Name",bg="yellow").place(x=50,y=52)
        e1=Entry(ra,border=5,width=25,bg="white",fg="red").place(x=150,y=50)

        l2=Label(ra,text="Last_Name",bg="yellow").place(x=50,y=92)
        e2=Entry(ra,border=5,width=25,bg="white",fg="red").place(x=150,y=90)

        l3=Label(ra,text="Father`s_Name",bg="yellow").place(x=50,y=132)
        e3=Entry(ra,border=5,width=25,bg="white",fg="red").place(x=150,y=130)

        l4=Label(ra,text="Mother`s_Name",bg="yellow").place(x=50,y=172)
        e4=Entry(ra,border=5,width=25,bg="white",fg="red").place(x=150,y=170)

        l5=Label(ra,text="Dob",bg="yellow").place(x=50,y=212)
        e5=Entry(ra,border=5,width=25,bg="white",fg="red").place(x=150,y=210)

        l6=Label(ra,text="Mobile No.",bg="yellow").place(x=50,y=252)
        e6=Entry(ra,border=5,width=25,bg="white",fg="red").place(x=150,y=250)

        l7=Label(ra,text="E-mail",bg="yellow").place(x=50,y=292)
        e7=Entry(ra,border=5,width=25,bg="white",fg="red").place(x=150,y=290)


        l8=Label(ra,text="Address",bg="yellow").place(x=50,y=332)
        e8=Entry(ra,border=5,width=25,bg="white",fg="red").place(x=150,y=330)

        but1=Button(ra,text="Submit",width=6,border=5,fg="red").place(x=150,y=370)
        but2=Button(ra,text="Cancel",width=6,command=quit,border=5,fg="red").place(x=230,y=370)


        ra.mainloop()
        






    def front(self):
        fr=Tk()
        fr.geometry("400x400")
        fr.title("Smart_IV_Stand")

        one=Frame(fr,bg="yellow",height=40,width=400).place(x=0,y=0)
        l1=Label(one,text="SMART IV STAND",bg="white",fg="red").place(x=160,y=10)

        
        two=Frame(fr,width=320,height=320,bg="lightgray").place(x=41,y=50)
        five=Frame(fr,width=320,height=15,bg="red").place(x=41,y=40)
        butt1=Button(two,text="Add New",border=4,width=8,fg="red",bg="white",command=self.ragi).place(x=54,y=70)
        butt2=Button(two,text="Update",border=4,width=8,fg="red",bg="white").place(x=154,y=70)
        butt3=Button(two,text="Rescipt",border=4,width=8,fg="red",bg="white").place(x=254,y=70)

        three=Frame(two,bg="red",height=10,width=320).place(x=42,y=110)
        butt4=Button(two,text="Wards",border=4,width=8,fg="red",bg="white").place(x=54,y=140)
        butt5=Button(two,text="Active IV ",border=4,width=10,fg="red",bg="white").place(x=154,y=140)
        butt6=Button(two,text="List",border=4,width=8,fg="red",bg="white").place(x=254,y=140)
        four=Frame(two,bg="red",height=10,width=320).place(x=42,y=190)

        butt7=Button(two,text="Developers",border=4,width=8,fg="red",bg="white").place(x=54,y=210)
        butt8=Button(two,text="Idea ",border=4,width=10,fg="red",bg="white").place(x=154,y=210)
        butt9=Button(two,text="Working",border=4,width=8,fg="red",bg="white").place(x=254,y=210)
        four=Frame(two,bg="red",height=10,width=320).place(x=42,y=250)
        
        butt7=Button(two,text="Developers",border=4,width=8,fg="red",bg="white").place(x=54,y=270)
        butt8=Button(two,text="Idea ",border=4,width=10,fg="red",bg="white").place(x=154,y=270)
        butt9=Button(two,text="Working",border=4,width=8,fg="red",bg="white").place(x=254,y=270)
        six=Frame(two,bg="red",height=10,width=320).place(x=42,y=320)
        


        fr.mainloop()





user=smart()

user.front()