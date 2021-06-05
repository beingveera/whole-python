import time 
from tkinter import *
from tkinter import messagebox 
  
  
root = Tk() 

root.title("Time Counter") 


fr=Frame(root)
fr.pack(side =TOP)

I=Label(fr,text="Timer Watch",bg="yellow",width=20,fg="red",bd=9).grid(row=1)


   
hour=StringVar() 
minute=StringVar() 
second=StringVar() 
   
hour.set("00") 
minute.set("00") 
second.set("00") 
 
 
h=Label(root,text="Hr :",fg="red")
h.place(x=100,y=80)

m=Label(root,text="Mn:",fg="red")
m.place(x=100,y=160)

s=Label(root,text="Sc :",fg="red")
s.place(x=100,y=240)


hourEntry= Entry(root, width=8, 
                 textvariable=hour) 
hourEntry.place(x=150,y=80) 
   
minuteEntry= Entry(root, width=8,
                   textvariable=minute) 
minuteEntry.place(x=150,y=160) 
   
secondEntry= Entry(root, width=8, 
                   textvariable=second) 
secondEntry.place(x=150,y=240) 
   
   
def submit(): 
    try: 
        temp = int(hour.get())**3600 + int(minute.get())*60 + int(second.get()) 
    except: 
        print("Please input the right value") 
    while temp >-1: 
          
        mins,secs = divmod(temp,60)  
        hours=0
        if mins >60: 
              
            hours, mins = divmod(mins, 60) 
          
        hour.set("{0:2d}".format(hours)) 
        minute.set("{0:2d}".format(mins)) 
        second.set("{0:2d}".format(secs)) 
        
        root.update() 
        time.sleep(1) 
   
        if (temp == 0): 
            messagebox.showinfo("Time Countdown", "Time's up ") 
          
        temp -= 1
  
btn = Button(root, text='Set Timer', bd='5', bg="red",fg="yellow",
             command= submit,width=14) 
btn.place(x = 140,y = 350) 
   
root.mainloop()