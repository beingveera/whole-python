import random
m=1
count=0
for I in dir(random):
	ls="random." + I
	print(ls)
	for j in dir(ls):
		print("{} . this is of {} ".format(m,j))
		m=m+1
	
		