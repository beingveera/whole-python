from tkinter import *
import requests

root=Tk()

val=StringVar()

def  fun():
	city=val.get()
	url= ("https://api.openweathermap.org/data/2.5/weather?q={}&appid=22e369740b71c8ad33feb5539808e281".format(city))
	data=requests.get(url). json()
	for i in data:
		print(i,' : ',data[i])
		print('\n')
	

lab=Label(root,text="Weather reporter",fg="red",bg="cyan",width=40,height=2)
lab.pack()


la=Label(root,text="City :-",fg="red",width=20, height= 1)
la.place(x=-70,y=100)

er=Entry(root,bd=5,bg="pink",fg="red", width=10, textvariable=val)
er.place(x=160,y=100)


but=Button(root,text="Submit",bd=5,fg="yellow",bg="red", command= fun)
but.place(x=165,y=200)

 
root.mainloop()