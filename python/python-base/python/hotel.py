def room():
	day=int(input('enter how much days u will stay:'))
	print('which type of room u want:')
	print('1.Simple')
	print('2.Midum')
	print('3.A.C.')
	print('4.Luxary')
	ch=int(input('enter your choice:'))
	amt =0
	if ch is 1:
		amt=day*400
		
	elif ch is 2:
		amt=day*600
	
	elif ch is 3:
		amt=day*800
		
	elif ch is 4:
		amt=day*1000
		
	else:
		print('invalid choice...')
def food():
	print('1.Break Fast')
	print('2.Lunch')
	print('3.Dinner')
	print('4.Fast Food')
	print('5.Deserts')
	ch1=int(input('enter your choice:'))
	if ch1 == 1:
		while(1):
			 print('1.Samosa')
		     print('2.Dhosa')
		     print('3.Khaman')
		     print('4.Kachori')
		     print('5.Phoha')
		     print('6.Chai')
		     print('7.Milk')
		     print('8.Coffee')
		     print('9.ideli')
		     print('10.Back')
		     ch2=int(input('Enter your choice:'))
		     if ch2 is 1:
		     	quan=int(input('enter the quantity:'))
		     	famt=quan*10
		     	print(famt)
		     elif ch2 is 2:
		     	quan=int(input('enter the quantity:'))
		     	famt=quan*30
		     	print(famt)
		     elif ch2 is 3:
		     	quan=int(input('enter the quantity:'))
		     	famt=quan*40
		     	print(famt)
		     elif ch2 is 4:
		     	quan=int(input('enter the quantity:'))
		     	famt=quan*15
		     	print(famt)
		     elif ch2 is 5:
		     	quan=int(input('enter the quantity:'))
		     	famt=quan*20
		     	print(famt)
		     elif ch2 is 6:
		     	quan=int(input('enter the quantity:'))
		     	famt=quan*10
		     	print(famt)
		     elif ch2 is 7:
		     	quan=int(input('enter the quantity:'))
		     	famt=quan*15
		     	print(famt)
		     elif ch2 is 8:
		     	quan=int(input('enter the quantity:'))
		     	famt=quan*15
		     	print(famt)
		     elif ch2 is 9:
		     	quan=int(input('enter the quantity:'))
		     	famt=quan*50
		     	print(famt)
		     elif ch2 is 10:
		           food()
	elif ch1 == 2:
	 print('1.Roti')
		     print('2.Rice')
	  	   print('3.Butter Milk')
	  	   print('4.Dal Makhni')
	  	   print('5.Salad')
	  	   print('6.Green Veg')
	  	   print('7.Back')
	  	   

print('Welcome to Hotal Veeras ')
while(1):
	print('1.Room')
	print('2.Food')
	ch8=int(input('Enter your choice:'))
	if ch8 == 1:
		room()
	elif ch8 == 2:
		food()
		
	