
from tkinter import *
from tkinter.ttk import *

# creating tkinter window 
root = Tk()
root.geometry("400x400")

# Adding widgets to the root window 
Label(root, text = 'Working of Smart iv', font =( 'Verdana', 15)).pack(side = TOP, pady = 10) 

# Creating a photoimage object to use image 
photo = PhotoImage(file = r"C:\\Users\\techno\\Desktop\\smart_iv_soft.png") 

# here, image option is used to 
# set image on button 
Button(root, text = 'Click Me !', image = photo,width=50).pack(side = TOP) 

mainloop() 
