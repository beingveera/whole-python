class convert:
    def data(self,val):
        self.out=val
        return "Ascii Charactor of {} is : {} ".format(self.out,chr(self.out))
x=int(input("Enter a Numerical value :"))
user=convert()
print(user.data(x))


