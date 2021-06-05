#ls,ms='veera','sharma'
#print(ls + ' '+ ms)
#print('veera is here {}'.format("lokesh"))
s=[56,12,74,32,85,41,12,89]
#print(sorted( s))
#print(sorted(s,reverse=True))
#s.sort(reverse=True)
#print(s)
nm="my name is Veera my age is"
#for word in nm.split():
#	print([word.upper()],[word.#lower()],len(word))
#print(s)
#m=tuple(s)
#print(m)
#print(tuple(sorted(m)))
#ls=[2,5,9,4,5,6,\
#5,9,1]
#print(ls)
#sum= 0
'''try:
      for I in range(10,100,10):
	         sum+=I
      print(sum)
except:
	print('veera')
finally:
	print('program chal Raha hai bhai')
'''

'''	 	 
while True:
	gh=input("one more : ")
	if gh == "yes":
		a=int(input())
		b=int(input())
		try:
			  c=a/b
			  print(c)
		except ZeroDivisionError:
			  print("you can't to this....")
	else :
		break
'''
"""
def data(a,b):
	return a*b
print(data(10,20))
"""
'''

def facto(n):
	f=1
	if n<=1:
		return f
	else:
		while n>0:
			f*=n
			n-=1
		return f
k=facto(3)
print(k)
'''
o=[]
g=lambda s : s
for I in s:
    y=g(I)
    o.append(y)
print(o)
    
