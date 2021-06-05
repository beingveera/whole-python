import re 
''''
with open("file.txt","w") as op:
    for i in range(1,10):
        ls=input()
        op.write(ls)
        op.write("\n")
'''
ps=[]
with open("file.txt","r") as op:
    for i in op:
        ls=op.readline()
        ps.append(ls)
js=[]
q = re.compile('\w+')
for i in ps:
    l=q.findall(i)
    js.append(l)


with open("final.txt","w") as op:
    for i in js:
        op.write(str(i))
        op.write("\n")
ks=[]
with open("final.txt","r") as st:
    for i in st:
        ls=st.read()
        ks.append(ls)
fg=[]
for i in ks:
    fg.append(i)
    fg.sort()
for i in fg:
    print(i)


    
