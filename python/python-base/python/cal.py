def add():
	an=0
	while True:
		ap=input("You want to Add more :")
		if ap == "y":
			fn=int(input("Enter the first No. :"))
			an=fn+an
		else:
			print("Your total addition is : {}".format(an))

def sub():
	an=0
	while True:
		ap=input("You want to Sub more :")
		if ap == "y":
			fn=int(input("Enter the first No. :"))
			an=fn+an
		else:
			print("Your total subtraction is : {}".format(an))
		



def conti():
	while True:
		us=input("You want Do More Operations :")
		if us =="y":
		    fi=input("Which type of function you want to perform :")
		    if fi == "add":
		    	add()
		    elif fi== "sub":
		    	sub()
		else:
			break


print("Which type you want to perform the operation :\n")
print("1.Continues")
print("2.Limited")
sc=int(input("Enter your Choice :"))
if sc==1:
	print("Continue")
	conti()
else:
	print("limited")
