from tkinter import  * 
import os
root=Tk()

root.title("Kernel")

bt1=Button(root,text="Shut Down",command=os.system('shutdown /s')).place(x=60,y=20)
bt2=Button(root,text="Restart",command=os.system('shutdown /r')).place(x=60,y=80)
bt3=Button(root,text="Sleep",command=os.system('shutdown /i')).place(x=60,y=140)
root.mainloop()