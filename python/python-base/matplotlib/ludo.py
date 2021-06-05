import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.random.randint(1,7,10),marker='o',markersize=7,color='red',label='player1')
plt.plot(np.random.randint(1,7,10),marker='o',markersize=7,color='blue',label='player2')
plt.plot(np.random.randint(1,7,10),marker='o',markersize=7,color='green',label='player3')
plt.plot(np.random.randint(1,7,10),marker='o',markersize=7,color='yellow',label='player4')
plt.legend()
plt.xlabel('no of turns')
plt.ylabel('dies output')
plt.title('basic prediction game')
plt.grid(True)
plt.figure(True)
plt.show()