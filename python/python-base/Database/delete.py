import sqlite3 as sq
db=sq.connect("office.db")
cr=db.cursor()
cr.execute("insert into techno (Id,Name,last,salery) VALUES(1,'lokesh','sharma',299);")
cr.execute("DELETE from techno where Id=1")
db.commit()
print("total no of row deleted : {}".format(db.total_changes))
db.close()