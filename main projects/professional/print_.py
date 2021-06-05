from __future__ import print_function
import keyword 

print('lokesh sharma',end="")
print([i for i in keyword.kwlist])

a,b,c=1,2,3
print(a,c,c)

a=b=c=2,4,2,4
print(a,b,c)

_ =20
lis=[1,3,_,5,7,96]
for _ in lis:
    print(_)
print(lis)

emp=[]
for i in keyword.kwlist:
    emp.append(i)
print(emp[::-1])


