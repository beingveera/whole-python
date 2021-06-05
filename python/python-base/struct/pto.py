import struct as st
#for I in dir(struct):
#	print(I)
i=int(input("How many integer data you want to encrypt :"))
j=int(input("How many float data you want to encrypt :"))
x="j"*j
y="i"*i
k=x+y
t=i+j
u=[]
z=0
while z != t:
	h=int(input())
	z+=1
	u.append(h)
u=tuple(u)
ty=st.pack("{}".format(k),"{}".format(u))

