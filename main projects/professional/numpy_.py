import numpy as np 

z=np.array([1,2,3,4,5,6])
#print(z)
u=np.array([[1,2,3,4,5,6],[12,23,34,45,56,67]])
#print(type(u))
n1=np.zeros((10,10))
#print(n1)
#print("\n\n")
n2=np.ones((3,4))
#print(n2)
n3=np.full((3,3),10)
#print(n3)
n5=np.arange(10,20)
#print(n5)
n6=np.arange(25,500,5)
#print(n6)
n7=np.random.randint(1,10,9)
#print(n7)
n8=np.array([[12,23,34,45,56,45],[3,5,6,85,3,34],[12,21,23,32,34,34]])
n8.shape=(6,3)
#print(n8)

n9=np.array([10,20,30,40,50])
n10=np.array([100,90,80,70,60])
n11=np.vstack((n9,n10))
n12=np.hstack((n9,n10))
n13=np.column_stack((n9,n10))
'''
print(n11)
print(n12)
print(n13)
'''

n14=np.array([10,20,30,40,40,50,60])
n15=np.array([100,90,80,70,60,50,40])
'''
print(np.intersect1d(n14,n15))
print(np.setdiff1d(n14,n15))
print(np.setdiff1d(n15,n14))
'''

n16=np.array([10,20,30])
n17=np.array([20,30,40])
'''
print(np.sum([n16,n17]))
print(np.sum([n16,n17],axis=0))
print(np.sum([n16,n17],axis=1))
'''
n18=np.array([10,20,30,40,50,60,70])
'''
print(n18+5)
print(n18-10)
print(n18*2)
print(n18/5)
'''

n19=np.random.randint(1,50,20)
'''
print(np.mean(n19))
print(np.std(n19))
print(np.median(n19))
'''

n20=np.array([10,20,30,40,50])
np.save('myarray',n20)
n21=np.load('myarray.npy')
print(n21)

