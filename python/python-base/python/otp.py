import random as rn 
otp='\0'
lis=['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(1,7):
    r=rn.randrange(0,62)
    otp=lis[r]+otp

print(otp)

user=input("Enter a number :")
if user in otp:
    print("Login SuccessFully...")
else:
    print("!!!!!!!!!")
    
