from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class smart:
		
	def ragi(self):
		
		ra=Tk()
		ra.geometry("400x460")
		ra.title("Ragistration")

		one1=Frame(ra,bg="yellow",height=40,width=400).place(x=0,y=0)
		two1=Frame(ra,bg="yellow",height=430,width=40).place(x=0,y=0)
		three1=Frame(ra,bg="yellow",height=430,width=40).place(x=360,y=0)
		four1=Frame(ra,bg="yellow",height=40,width=400).place(x=0,y=430)

		l11=Label(ra,text=" First Name ",fg="blue",bg="pink").place(x=50,y=72)
		e11=Entry(ra,border=5,bg="lightgray",fg="red",width=25).place(x=150,y=70)

		l21=Label(ra,text=" Last Name ",fg="blue",bg="pink").place(x=50,y=112)
		e21=Entry(ra,border=5,bg="lightgray",fg="red",width=25).place(x=150,y=110)

		l31=Label(ra,text=" Father`s Name ",fg="blue",bg="pink").place(x=50,y=152)
		e31=Entry(ra,border=5,bg="lightgray",fg="red",width=25).place(x=150,y=150)

		l41=Label(ra,text=" Mother`s Name ",fg="blue",bg="pink").place(x=50,y=192)
		e41=Entry(ra,border=5,bg="lightgray",fg="red",width=25).place(x=150,y=190)

		l51=Label(ra,text=" Date of Birth ",fg="blue",bg="pink").place(x=50,y=232)
		e51=Entry(ra,border=5,bg="lightgray",fg="red",width=25).place(x=150,y=230)

		l61=Label(ra,text=" Mobile No. ",fg="blue",bg="pink").place(x=50,y=272)
		e61=Entry(ra,border=5,bg="lightgray",fg="red",width=25).place(x=150,y=270)

		l71=Label(ra,text=" E-mail ",fg="blue",bg="pink").place(x=50,y=312)
		e71=Entry(ra,border=5,bg="lightgray",fg="red",width=25).place(x=150,y=310)

		l81=Label(ra,text=" Address ",fg="blue",bg="pink").place(x=50,y=352)
		e81=Entry(ra,border=5,bg="lightgray",fg="red",width=25).place(x=150,y=350)

		but11=Button(ra,text="Submit" ,width=9,border=5,bg="white",fg="red").place(x=120,y=390)
		but21=Button(ra,text="Cancel" ,width=9,border=5,bg="white",fg="red",command=quit).place(x=220,y=390)

		

		



		ra.mainloop()

	lk="Mr. Latif Khan sir is mentor of the Smart iv Stand , he is such a very hardworking guy."
	
	def latifs(self):
			messagebox.showinfo("Mr. Latif Sir",self.lk)
	
	def ateek(self):
			messagebox.showinfo("Mohammad Ateek Samma","Team Leader")
		
	def shubham(self):
			messagebox.showinfo("Shubham Vagrecha","Hardware Controller")
	
	def sheetal(self):
			messagebox.showinfo("Sheetal Sharma","Content Writer")
	
	def lokesh(self):
			messagebox.showinfo("Lokesh Sharma"," {} ".format(self.lk))

	def team(self):
		
		te=Tk()

		te.geometry("400x450")
		te.title("Team Members")
		one2=Frame(te,bg="yellow",height=40,width=400).place(x=0,y=0)
		l12=Label(te,text=" MEDI SQUAD ",bg="white",fg="red",font =( 'Verdana', 10)).place(x=160,y=10)
		two2=Frame(te,bg="yellow",height=430,width=40).place(x=0,y=0)
		three2=Frame(te,bg="yellow",height=430,width=40).place(x=360,y=0)
		four2=Frame(te,bg="yellow",height=40,width=400).place(x=0,y=415)

		five2=Frame(te,bg="lightgray",width=150,height=375).place(x=40,y=40)
		six2=Frame(te,bg="lightpink",width=150,height=375).place(x=210,y=40)

		but12=Button(te,text="Mr. Latif Khan Sir ",border=3,width=15,command=self.latifs).place(x=50,y=60)
		la12=Label(te,text=" Team Mentor ",bg="white",fg="red",width=15).place(x=220,y=63)

		but22=Button(te,text="Mohammad Ateek ",border=3,width=15,command=self.ateek).place(x=50,y=120)
		la22=Label(te,text=" Team Leader ",bg="white",fg="red",width=15).place(x=220,y=122)

		but32=Button(te,text="Shubham Vagrecha",border=3,width=15,command=self.shubham).place(x=50,y=180)
		la32=Label(te,text=" Hardware Controller ",bg="white",fg="red",width=15).place(x=220,y=182)

		but42=Button(te,text="Sheetal Sharma",border=3,width=15,command=self.sheetal).place(x=50,y=240)
		la4=Label(te,text=" Content Writer",bg="white",fg="red",width=15).place(x=220,y=242)

		but52=Button(te,text="Lokesh Sharma",border=3,width=15,command=self.lokesh).place(x=50,y=300)
		la52=Label(te,text=" Software Controller",bg="white",fg="red",width=15).place(x=220,y=302)


		te.mainloop()

	
	def working(self):

		wo=Tk()
		Label(wo, text = 'Working of Smart iv', font =( 'Verdana', 15)).pack(side = TOP, pady = 10) 
		photo = PhotoImage(file = r"C:\\Users\\techno\\Desktop\\smart_iv_soft.png") 
		Button(wo, text = 'Click Me !', image = photo).pack(side = TOP) 
		wo.mainloop() 














	def front(self):
		fr=Tk()
		fr.geometry("400x400")
		fr.title("Smart IV Stand")
		one=Frame(fr,bg="yellow",height=40,width=400).place(x=0,y=0)
		l1=Label(one,text="SMART IV STAND",bg="white",fg="red",font =( 'Verdana', 10)).place(x=160,y=10)

		two=Frame(fr,bg="yellow",height=400,width=40).place(x=0,y=0)
		three=Frame(fr,bg="yellow",height=400,width=40).place(x=360,y=0)
		four=Frame(fr,bg="yellow",height=40,width=400).place(x=0,y=360)

		five=Frame(fr,height=320,width=320,bg="lightgray",border=5).place(x=40,y=40)
		
		but1=Button(fr,text="Ragistration",border=5,bg='white',fg="red",width=10,command=self.ragi).place(x=50,y=70)
		but2=Button(fr,text="Update",border=5,bg='white',fg="red",width=10).place(x=150,y=70)
		but3=Button(fr,text="List",border=5,bg='white',fg="red",width=10).place(x=250,y=70)

		but4=Button(fr,text="Wards",border=5,bg='white',fg="red",width=10).place(x=50,y=140)
		but5=Button(fr,text="Active IV",border=5,bg='white',fg="red",width=10).place(x=150,y=140)
		but6=Button(fr,text="Alerts",border=5,bg='white',fg="red",width=10).place(x=250,y=140)

		but7=Button(fr,text="Server Data",border=5,bg='white',fg="red",width=10).place(x=50,y=210)
		but8=Button(fr,text="Messages",border=5,bg='white',fg="red",width=10).place(x=150,y=210)
		but9=Button(fr,text="Total IV",border=5,bg='white',fg="red",width=10).place(x=250,y=210)

		but10=Button(fr,text="Developer",border=5,bg='white',fg="red",width=10).place(x=50,y=280)
		but11=Button(fr,text="Working",border=5,bg='white',fg="red",width=10,command=self.working).place(x=150,y=280)
		but12=Button(fr,text="Team",border=5,bg='white',fg="red",width=10,command=self.team).place(x=250,y=280)
			

		fr.mainloop()

user=smart()
user.front()