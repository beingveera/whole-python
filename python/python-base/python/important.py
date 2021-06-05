'''ls=(1,2,3,"on")
ps=("python","Instagram")
ns=ls+ps
ns=set(ns)
print(ns)
'''
'''
class calc:
	def __init__(self):
		pass
	def sum(self,a1,a2):
		return a1+a2
	def sub(self,a1,a2):
		return a1-a2
init=calc()
print("Sum is : ",init.sum(20,30))
print("Subtraction is :",init.sub(20,30))
'''
'''
l="hello\
user"
print(l)
'''
'''
import json
std={
"Name" :"lokesh",
"Roll_no":"18egics051",
"Grade" :"A",
"Age" : "19",
"Subject" : ["computer graphics","maths"]
}
with open("data.json","w") as we:
	json.dump(std,we)
with open("data.json","r") as p:
	f=json.load(p)
	print(f.get('Name'))
	print(f)
'''
'''
import random as rn
s="abcdefghijklmnopqrstuvwxyz1234567890@#$&?\
£¢€¥π¶∆©®ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passlen=8
password="".join(rn.sample(s,passlen))
print("Your password is : ",password)
'''
