import secrets as p
#ps=p.randbelow(20)
#print(ps)
#hl=p.randbits(7)
#print(hl)
import string
al=string.ascii_letters + string.digits
for i in range(1,7):
	ps=' '.join(p.choice(al))
	print(ps,end="")