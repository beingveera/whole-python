class num:
    def rev(self,x):
        self.a=x
        return "Reverse of {} is :  {}  ".format(self.a,self.a[::-1])
user=num()
z=input("Enter a number :")
print(user.rev(z))


