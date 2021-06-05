import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()

x=fig.add_subplot(111, polar=True)

r=np.arange(0,1,0.001)
theta=4*np.pi*r
line=x.plot(theta,r,color='blue',lw=3)

ind=800

thisr,thistheta=r[ind],theta[ind]

x.plot([thistheta],[thisr],'o')

x.annotate('polar',
           
           xy=(thistheta,thisr),
           xytext=(0.05,0.05),
           arraow=dict(facecolor='black',shirnk=0.5),
           horizontalalignment='left',
           verticalalignment='bottom'
           
           
           
           
           )

plt.show()