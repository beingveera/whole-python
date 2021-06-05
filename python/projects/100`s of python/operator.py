class operator:
    def oper(self,x,y,z):
        self.a=x 
        self.b=y 
        self.c=z 
        if self.c == "+":
            return 'Sum of {} and {} is : {} '.format(self.a,self.b,self.a + self.b)
        elif self.c == "-":
            return 'Sub of {} and {} is : {} '.format(self.a,self.b,self.a - self.b)
        elif self.c == "/":
            return 'div of {} and {} is : {} '.format(self.a,self.b,self.a / self.b)
        elif self.c == "*":
            return 'Mul of {} and {} is : {} '.format(self.a,self.b,self.a * self.b)
        elif self.c == "%":
            return 'Mod of {} and {} is : {} '.format(self.a,self.b,self.a % self.b) 
        elif self.c == "^":
            return 'Pow of {} and {} is : {} '.format(self.a,self.b,self.a ** self.b)     
user=operator()
val1,val2,sign=int(input("Enter the value of x : ")),int(input("Enter the value of y : ")),input("Enter the Sign : ")
print(user.oper(val1,val2,sign))