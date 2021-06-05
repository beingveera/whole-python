import sqlite3 as sq
db=sq.connect("main.db")
cr=db.cursor()
hu=cr.execute("SELECT Uname FROM GITS")
for I in hu:
	print(I)
db.commit()