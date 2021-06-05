class printl:
    def data(self,x):
        self.y=x
        return str(self.y )
user=printl()
val=int(input())
print(user.data(val))

