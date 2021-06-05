import numpy as np

'''
print(np.__version__)
print(np.__doc__)
for i in dir(np):
    print(i)
'''

'''
l=list(range(1,10))
print(l)
print(type(l))

print([str(i) for i in l])
print(type(i))
'''

'''
ls=['lokesh',True,123,54.789,'345']
for i in ls:
    print('{} : {} '.format(i,type(i)))

'''
    

'''
print(type(np.array([1,2,3,4])))
print([range(1,i+3) for i in [1,2,3]])
print(np.array([range(i,i+3) for i in [1,2,3]]))
'''

'''
k=np.zeros(9,dtype='int')
k=np.zeros((3,3),dtype='int')
print(k)
'''

'''
k=np.ones(9,dtype='int')
print(k)
k=np.ones((3,3),dtype='int')
print(k)
'''

'''
k=np.full((3,3),10)
print(k)
'''

'''
k=np.arange(0,20,2)
k.resize((3,3))
print(k)
'''

'''
k=np.linspace(0,10,dtype='int')
k.resize((4,10))
print(k)
'''

'''
print((np.random.random(5)))
print(np.random.randint(1,10,5))
print(np.random.rand(1,10,4))
'''

'''
k=np.random.normal(5,10,(3,3))
print(k)
l=np.random.randint(1,10,(3,3))
print(l)
print(l.itemsize)
'''


'''
print(np.eye(5))
print(np.empty((3,3)))
print(np.zeros((3,3)))
'''

'''
print(np.random.randint(10,size=5))
print(np.random.randint(10,size=(3,3)))
'''

'''
d=np.random.randint(1,10,(3,3))
print(d)
print(d[1][1])
'''
'''
p=np.arange(1,10)
p.resize(3,3)
print(p)
print('\n')
for i in range(0,3):
    for j in range(0,3):
            p[i][j]=p[j][i]
            
print(p)
'''

'''
l=np.resize(1,2)
print(l.copy())
print(l)
'''
'''
x=np.arange(1,5)
y=np.arange(5,10)
z=np.concatenate([x,y])
print(z)
'''
'''
m=[12,3,4,5,6,5]
print(len(m))
print([m>[90]])
'''

'''
z=np.arange(1,10)
print(z)
x1,x2,x3=np.split(z,[2,2])
print(x1,x2,x3)
'''

'''
z=np.random.seed(4)
print(z)
'''

'''
l=np.random.rand(50)
for i in l:
    print(np.sin(i))
'''
'''
ls=[[2,3,4],[3,4,5]]
print(np.shape(ls))
'''

'''
k=np.arange(1,10)
print(k)
print(np.any(10<k))
print(np.all(k<10))
'''
