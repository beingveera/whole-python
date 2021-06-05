import sqlite3 as sq
db=sq.connect("main.db")
cr=db.cursor()
x=input()
y=input()
cr.execute("insert into veera(Uname , upass ) VALUES( ' "+x+" ',' "+y+" ')")
db.commit()
db.close()
print('veera')