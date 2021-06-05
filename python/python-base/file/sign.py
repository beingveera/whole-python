with open("sign.txt","w") as lp:
	for i in range(1,200000):
#		o=str(i)
		o=chr(i)
		lp.write("The value of {} is :  {}".format(i,o))
		lp.write("\n")