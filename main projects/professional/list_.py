
ap=(1,2,3,4,5,6)
op=list(ap)
#print(op)

ps=[]
for i in range(65,70):
    p=chr(i)
    p=list()
    ps.append(p)
    #print(ps)
ls=[]
js=[]
[ls.append(i) for i in range(20,30)]
#print(ls)

for i in range(1,10):
    ls.append(i)
#print(ls)
#print(ps[0].append(ls))

js.append(ls)
#print(js)

a=[1,2,3,4,5]
b=[0,9,8,7,6]
a.extend(b)
#print(a)

'''
c=[]
c.append(range(1,10))
for i in c:
    #print(i)
'''

d=[]
for i in range(0,10):
    d.insert(i,i+i)
print(d)