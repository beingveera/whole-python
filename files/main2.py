import matplotlib.pyplot as plt
import math
ls=[]
k=0
while True:
    if k<10:
        ls.append(math.sin(k))
        k+=0.1
    else:
        break
    plt.plot(ls)
    plt.grid(True,which='major',axis='y')

l=ls[0]
for i in range(len(ls)):
    if l < ls[i]:
        l=ls[i]
print(math.asin(l))
print(math.sin(1.5415926535897915))
plt.show()
    