class grade:
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.out=self.a + self.b + self.c + self.d + self.e + self.f
    def pers(self):
        mar=self.out/6
        if mar > 90:
            return "A++"
        elif mar < 90 and mar>75:
            return "A+"  
        elif mar < 75 and mar>60:
            return "A" 
        elif mar < 60 and mar>45:
            return "B"   
        elif mar < 45 and mar>33:
            return "C"
        else:
            return "F"
p,q,r,s,t,u=int(input("Enter marks of Maths :")),int(input("Enter marks of English :")),int(input("Enter marks of Physics :")),int(input("Enter marks of Chemsitry :")),int(input("Enter marks of Computer :")),int(input("Enter marks of Hindi :"))
student=grade(p,q,r,s,t,u)
tot=student.pers()
print("\nYour Grade is {} ".format(tot))
    
    