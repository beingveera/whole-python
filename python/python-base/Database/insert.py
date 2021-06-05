import sqlite3 as sq
db=sq.connect("main.db")
cr=db.cursor()
cr.execute("insert into veera(Uname, upass ) VALUES('LOKESH','BHATT')")
db.commit()
db.close()
print('insert data...')

