import matplotlib.pyplot as plt
import numpy as np
ls=[]
i=0
for i in range(1,20,2):
	ls.append(i)
	plt.plot(ls,marker='*',markersize=i+1)
plt.grid(True)
plt.show()