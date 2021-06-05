class day:
    def work(self,z):
        self.a=z
        return self.a * 20 - 15

class work:
    def sel(self,fin):
        self.total=fin
        return (self.total * 100)/2

worker=work()
data=day()
din=int(input("Enter your Working days in a month : "))
pap=data.work(din)
o=worker.sel(pap)
print("Your Total Salery is {} $ of {} days !!! ".format(o,din))



        