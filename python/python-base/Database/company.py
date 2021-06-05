import sqlite3 as sq
db=sq.connect("company.db")
cr=db.cursor()
while True :
	entry=input("you want to enter more data :")
	if entry=='yes':
		id=input('Enter your Id :')
		nm=input("Enter your first Name :")
		ls=input("Enter your last name :")
		sal=input("Enter your salery :")
		cr.execute("create table data (Id text,Name text,last text,salery text)")
		cr.execute("insert into data(Id ,Name ,last ,salery ) VALUES(' "+id+" ' ,' "+nm+" ',' "+ls+" ',' " +sal+ " ')")
		db.commit()
	else:
		db.close()
		exit()     
      
print('veera')