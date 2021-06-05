import re
ls=[]
gh=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
gv=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
'''
with open('lang.txt') as dp:
    for i in dp:
        if i.isalnum:
            ls.append(i)
ps=[]
for i in range(1,100):
    obj=re.findall('[A-Za-z]',ls[i])
    ps.append(obj)
'''
'''
with open('data.txt','w') as pp:
    for i in ps:
        j=str(i)
        n=len(j)
        pp.write(j[1:n-1])
        pp.write('\n')
'''
val=''
nm=[]
with open('data.txt','r') as pt:
    for i in pt:
        for j in i:
            if j in gh or j in gv:
                val=val + j
    nm.append(val)
              
                

            
print(nm)





