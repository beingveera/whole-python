string =input("Enter your String : ")
ls=['a','e','i','o','u']
a,e,i,o,u=0,0,0,0,0
for n in string:
    if n == 'a':
        a+=1
    elif n == 'e':
        e+=1
    elif n == 'i':
        i+=1
    elif n == 'o':
        o+=1
    elif n == 'u':
        u+=1
print("a:{}\ne:{}\ni:{}\no:{}\nu:{}".format(a,e,i,o,u))
if a==0 and e==0 and i==0 and o==0 and u==0:
    print(0)
else:
    for k in string:
        if k not in ls:
            print(k,end="")