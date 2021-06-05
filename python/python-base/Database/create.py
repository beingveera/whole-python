import sqlite3 as sq
db=sq.connect("main.db")
cr=db.cursor()
cr.execute("create table veera(Uname text, upass text)")
db.commit()
db.close()
print('veera')