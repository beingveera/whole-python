from tkinter import * 


class model:
    val=StringVar
    
    
    def printing(self):
        new=textvariable.get
        print(new)
        
    def __init__(self):
        a.self =Tk()
        a.self.title('Marrige')
        a.self.geometry('400x400')
        frame1=Frame(a.self,bg='gray',height=40,width=400).place(x=0,y=0)
        e1=Entry(a.self,width=30,fg='red',bg='yellow',border=4,textvariable=self.val).place(x=100,y=60)
        b1=Button(width=5,fg='yellow',bg='red',border=3,text='Submit',command=self.printing).place(x=160,y=100)
        mainloop()
    
    
        
        
    

obj=model()
    