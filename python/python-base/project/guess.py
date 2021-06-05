import random as rn
count=10
print("=====================================================")
print("		NUMBER GUESSING GAME")
print("=====================================================")
while True :
	no=rn.randint(1,10)
	ch=int(input("Guess the number :"))
	print("\t\t\t\t\t\t{}".format(count))
	if count == 0:
		print()
		print('You lose the game...!!!')
		break		
	if no >= ch:
		print("			Guess value is low")
		count-= 1
		print()
	elif no <= ch:
		print("			Guess value is High")
		count -=1
		print()
	elif no == ch: 
		print("			You guess the number ...")
		print("			You Win...!!!!!!!")
		print()
		count -=1
		