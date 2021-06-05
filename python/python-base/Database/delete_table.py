import sqlite3 as sq
db=sq.connect("main.db")
cr=db.cursor()
cr.execute("DROP TABLE GITS")
db.commit()