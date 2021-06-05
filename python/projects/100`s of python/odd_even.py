class person:
    def __init__(self,num):
        self.num=num
    def pr(self,num):
        if self.num % 2 == 0:
            return True
        else:
            return False 
p=int(input("\nEnter a number : "))
user=person(p)
x=user.pr(p)
if x is True:
    print("{} is Even Number...!!! ".format(p))
else:
    print("{} is Odd Number ...!!!".format(p))
