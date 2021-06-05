import numpy as np
import matplotlib.pyplot as plt
from pylab import *
x = np.linspace(-5, 5, 50)
y1 = x**2
y2 = x**3
fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2)
ax.legend(loc=2)
plt.show()
