from tkinter import *
root= Tk()

l=Scale(root,bg="red",fg="yellow",bd=5,digit=3,width=30,length=900,orient="vertical",sliderlength=20,showvalue=900, relief="sunken",state='active',sliderrelief="sunken", repeatdelay=3,tickinterval=10,troughcolor="blue", resolution= 2,takefocus=3,to=1000,label="scalebar")
l.pack(padx=30,pady=30,fill="x")


root.mainloop()