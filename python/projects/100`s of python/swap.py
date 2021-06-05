class swap:
    def num(self,x,y):
        self.a=x
        self.b=y
        return(self.b,self.a)
val1,val2=int(input("Enter the value of x : ")),int(input("Enter the value of y : "))
user=swap()
ls=[]
for i in user.num(val1,val2):
    ls.append(i)
for i in ls:
    print('\nvalue of x is : {}\nvalue of y is : {}'.format(ls[0],ls[1]))
    break

