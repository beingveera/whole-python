import re 

for i in range(1):
    with open("number.txt","r") as data:
        ls=data.readlines()    

p=re.compile("\d+")
ps=(p.findall(ls))
print(ps)
    