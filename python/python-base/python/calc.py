x=int(input('enter a number:'))
y=int(input('enter a number:')) 
def add():
	z=x+y
	print(z)
def sub():
	z=x-y
	print(z)
def mul():
	z=x*y
	print(z)
def div():
	z=x/y
	print(z)
def pow():
	z=x**y
	print(z)
def mod():
	z=x%y
	print(z)
while(1):
	print('Menu')
	print('1.Add')
	print('2.Sub')
	print('3.Multi')
	print('4.Div')
	print('5.pow')
	print('6.mod')
	print('7.Exit')
	ch=int(input('entet your choice:'))
	if ch == 1:
	    add()
	elif ch == 2:
		sub()
	elif ch == 3:
	    mul()
	elif ch == 4:
	    div()
	elif ch == 5:
		pow()
	elif ch == 6:
		mod()
	elif ch == 7:
		exit(0)
	else:
		print('invalid choice......\n ')
		
			