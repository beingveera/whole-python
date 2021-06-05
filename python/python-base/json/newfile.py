import random as rn
import json
l=open("password.txt","w")
for I in range(1,1000):	
	s="1234567890"
	pl=4
	password="".join(rn.sample(s,pl))
	l.write("password is : {}".format(password))
	l.write("\n")
	print(password)
	