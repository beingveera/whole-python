import matplotlib.pyplot as plt
import numpy as np

xaxis=np.linspace(0,np.pi*2,100)
yaxis=np.sin(xaxis)

plt.plot(xaxis,yaxis)
plt.ylabel('sin(x)')

plt.show()