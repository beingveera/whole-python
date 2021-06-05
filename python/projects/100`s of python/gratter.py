class A:
    def one(self,x):
        self.val1=x

class B(A):
    def two(self,y):
        self.val2=y

class C(B):
    def three(self,x,y,z):
        self.val1=x
        self.val2=y
        self.val3=z 

        if self.val1 > self.val2 and self.val1>self.val3:
            return "\n{} is Gretest...!!! ".format(self.val1)

        elif self.val2 > self.val1 and self.val2 >self.val3:
            return "\n{} is Gretest...!!! ".format(self.val2) 

        else:
            return "\n{} is Gretest...!!! ".format(self.val3)
user=C()
a,b,c=int(input("Enter Value of X : ")),int(input("Enter Value of Y : ")),int(input("Enter Value of Z : "))
print(user.three(a,b,c))
