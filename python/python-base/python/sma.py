import re 
import random as rn 
strs=input("Enter your String : ")

a=re.compile("[a-z]")
x=a.findall(strs)
print("Total Lower Case Charactor  in String : {} ".format(len(x)))
print("List of Lower Case Charactor is Sting :  {} ".format(x))

b=re.compile("[A-Z]")
y=b.findall(strs)
print("Total Upper Charactor in String : {} ".format(len(y)))
print("List of Upper Case Charactor is Sting :  {} ".format(y))

c=re.compile("\d+")
z=c.findall(strs)
print("Total Number in String : {} ".format(len(z)))
print("List of Numbers is Sting :  {} ".format(z))

d=re.compile("\W+")
w=d.findall(strs)
print("Total Spacial Charactor  in String : {} ".format(len(w)))
print("List of Special Charactor is Sting :  {} ".format(w))
