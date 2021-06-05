import matplotlib.pyplot as plt
import random
ls=[]
ps=[]
#inp=int(input('Enter a limit :'))
x=0
while x != 10:
	y=random.randint(1,20)
	ls.append(y)
while x != 10:
	z=random.randint(1,20)
	ps.append(z)
	plt.plot(ls,ps)
plt.show()
