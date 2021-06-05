class temp:
    def degree(self,x,ty):
        self.a=x
        self.b=ty
        if ty =="k":
            return "{} *C ==> {} *K  Temprature".format(self.a,self.a + 273.15)
        elif ty =="c":
            return "{} *F ==> {} *C  Temprature".format(self.a,(self.a - 32)*5/9)
        elif ty =="f":
            return "{} *C ==> {} *F  Temprature".format(self.a,(self.a +32)*9/5) 
user=temp()
temprature,mes=int(input("Enter the Value of Temprature : ")),input("Enter the Messure of Temprature : ")
print(user.degree(temprature,mes))