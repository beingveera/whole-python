class details:
    def data(self,fname,lname,mail,passw,cpassw):
        self.first=fname
        self.last=lname
        self.email=mail
        self.password=passw
        self.cpass=cpassw
        return '\n {} \n {} \n {} \n {} \n {} '.format(self.first,self.last,self.email,self.password,self.cpass)
user=details()
ls=[]
for i in range(1,6):
    i=input()
    ls.append(i)
print(user.data(ls[0],ls[1],ls[2],ls[3],ls[4]))










