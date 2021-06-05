import sqlite3 as sq
db=sq.connect("main.db")
cr=db.cursor()
cr.execute("create table yu (Id INTEGER PRIMARY KEY AUTOINCREMENT , password text)")
db.commit()