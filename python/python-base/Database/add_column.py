import sqlite3 as sq
db=sq.connect('main.db')
cr=db.cursor()
cr.execute("ALTER TABLE house ADD COLUMN chair")
db.commit()
