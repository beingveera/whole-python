import matplotlib.pyplot as plt
import numpy as np 
from matplotlib import lines

'''
x=np.linspace(1,10,100)
x_sin=np.sin(x)
x_cos=np.cos(x)
plt.plot(x,x_sin)
plt.plot(x,x_cos)
plt.grid(True)
plt.show()
'''

'''
x=np.linspace(0,10,100)
fig=plt.figure()
plt.plot(x,np.sin(x),'-')
plt.plot(x,np.cos(x),'--')
fig.savefig('graph.png')
plt.show()
'''

'''
fig=plt.figure()
plt.subplot(211)
plt.plot(np.arange(1,10,5))

plt.subplot(212)
plt.plot(np.arange(10,20))
plt.show()
'''

'''
fig=plt.figure()
plt.subplot(211)
plt.plot(np.linspace(0,10,100),np.sin(np.linspace(0,10,100)))

plt.subplot(212)
plt.plot(np.linspace(0,10,100),np.cos(np.linspace(0,10,100)))
plt.show()
'''

'''
plt.style.use('seaborn-whitegrid')
plt.plot([1,2,3])
plt.show()
'''

'''
k=['red','blue','green','pink','gray','purple','orange','yellow','brown']
l=np.linspace(0,10,100)
for i in range(0,8):
    plt.plot(l,np.sin(l-i),color=k[i])
    '''
    
x=np.linspace(0,10,100)
plt.plot(x,linestyle='solid')
plt.plot(x+5,linestyle='dashed')
plt.plot(x+10,linestyle='dashdot')
plt.plot(x+15,linestyle='dotted')
plt.plot(x+20,linestyle='solid')
plt.plot(x+25,linestyle='dashed')
plt.plot(x+30,linestyle='dashdot')
plt.plot(x+35,linestyle='dotted')
    
    
