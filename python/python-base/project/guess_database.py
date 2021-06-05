import random as rn
count=2
res="Win"
with open("guess.txt","w") as lp:
	lp.write("Name\t\t\t\t Result\t\t \t\tChanses")
	lp.write("\n")
	nm=input("Enter your Name : ")
	print("=======\
==============================================")
	print("		NUMBER GUESSING GAME")
	print("=============\
========================================")
	print("\t\t\t\t\t     chances")
	for i in range(1,4):
		no=rn.randint(1,10)
		ch=int(input("Guess the number :"))
		print("\nYour previous No is {}: ". format(no))
		print("\t\t\t\t\t\t{}".format(count))
		if count == 0:
			print("===========\
==========================================")
			print(' {} , YOU LOSE THE GAME ...!!!'.format(nm.upper()))
			res="Lose"
			print("==========\
===========================================")
			break		
		if no >ch:
			print("			Guess value is low")
			count-= 1
			print()
		elif no <ch:
			print("			Guess value is High")
			count -=1
			print()
		elif no == ch: 
			print("===========\
==========================================")
			print(' {} , YOU WIN THE GAME ...!!!'.format(nm.upper()))
			print("==========\
===========================================")
			print()
			count -=1
	lp.write("{}\t\t\t\t\t{}\t\t\t\t\t{}".format(nm,res,count))

			
		