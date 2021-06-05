import sqlite3 as sq 
import random as rn
import numpy as np


nm=['lokesh','techno','veera','suravi','om','janvi','maa','paa','maate']
add=['bhilwara','mandal','udaipur','londan','bangluru','hedrabaad','kerla','jaipur']
   
con=sq.connect("main.db")
cur=con.cursor() 

   
for i in range(1,5):
    ide=rn.randint(1,100)
    age=rn.randint(20,80)
    sal=rn.randint(25000,100000)
    val=rn.randint(0,len(nm)-1)
    real=nm[val]
    val1=rn.randint(0,len(add)-1)
    real1=add[val1]
    cur.execute("INSERT INTO student(id,NAME,AGE,ADDRESS,SALERY) VALUES(20,'techno',20,'veera',20000)");
    con.commit()
con.close()




#cur.execute('''CREATE TABLE student(
#        id INT PRIMARY KEY NOT NULL,
#        NAME TEXT NOT NULL,
#        AGE INT NOT NULL,
#        ADDRESS CHAR(50),
#        SALERY  REAL
#        );''')
