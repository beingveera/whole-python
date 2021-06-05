import matplotlib.pyplot as plt
import random 
import time 

colors=['red','blue','yellow','green','black','gray','purple','orange','brown','pink']
ls=[]
ps=[]
lis_1=[] 
lis_2=[] 
lis_3=[]

for i in range(1,10):
    k=random.randint(1,10)
    print(k)
    if k>=1 and k<4:
        lis_1.append(k)
    elif k>=4 and k<7:
        lis_2.append(k)
    elif k>=7 and k<=10:
        lis_3.append(k)
        
    ls.append(k)
    plt.plot(ls,'o-',color=colors[k-1], label='Motion Intensity')
    plt.grid(axis='y')
    plt.xlabel(' Number Of Motion Detect ')
    plt.ylabel('Density of Motion ')
    plt.legend()
    plt.show()
    
ps.append(len(lis_1))
ps.append(len(lis_2))
ps.append(len(lis_3))

print('No of Count of Low Motion : {}'.format(len(lis_1)))
print('No of Count of Medium Motion : {}'.format(len(lis_2)))
print('No of Count of High Motion : {}'.format(len(lis_3)))

explode = (0.1, 0.1, 0.1) 
labels=['low or None Motion','Medium Motion', 'High Motion']

plt.pie(ps,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True, startangle=90)
plt.legend()

plt.show()
