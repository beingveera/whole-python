# -*- coding: utf-8 -
from tkinter import *
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

root=Tk()
root.geometry('400x400')
root.title('Whatsapp Bomber')
root.resizable(False, False)

driver = webdriver.Chrome(r'C:\\Users\\techno\\Desktop\\chromedriver.exe')


name=StringVar()
amount=IntVar()
msg=StringVar()

def find():
    Name=name.get()
    Amount=amount.get()
    Msg=msg.get()
    print(Name)
    print(Amount)
    print(Msg)
    
    driver.get("https://web.whatsapp.com/") 
    wait = WebDriverWait(driver, 600) 
    
    target = '"{}"'.format(Name)
    string = "{}".format(Msg)
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
    group_title.click() 
    inp_xpath ='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) 
    for i in range(Amount): 
        input_box.send_keys(string + Keys.ENTER) 
        time.sleep(1)


f1=Frame(root,height=30,width=400,bg='lightgreen',bd=5).place(x=0,y=0)
l1=Label(f1,text="Whatsaap Bomber",bg="white",fg='black').place(x=150,y=7)
       
f2=Frame(root,height=30,width=400,bg='lightgreen',bd=5).place(x=0,y=60)
l1=Label(f2,text="Name of User",bg="white",fg='black').place(x=10,y=65)
e1=Entry(f2,bd=3,width=30,textvariable= name).place(x=120,y=63)

f3=Frame(root,height=30,width=400,bg='lightgreen',bd=5).place(x=0,y=130)
l2=Label(f3,text="No. of Messages",bg="white",fg='black').place(x=10,y=135)
e2=Entry(f3,bd=3,width=10,textvariable= amount).place(x=120,y=133)

f4=Frame(root,height=100,width=400,bg='lightgreen',bd=5).place(x=0,y=200)
l3=Label(f2,text="Message",bg="white",fg='black').place(x=10,y=220)
text=Entry(f4,width=34,bd=3,textvariable=msg).place(x=120,y=210)

b1=Button(root,text='Submit',bd=3,height=1,width=10,bg='lightgreen',fg='white',command=find).place(x=160,y=350)

root.mainloop()
    






       