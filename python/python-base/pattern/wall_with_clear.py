from subprocess import call
import os
import time
def clear(): 
    _ = call('clear' if os.name =='posix' else 'cls') 

gh=int(input("Enter a limits :"))
ji=int(input("Enter a value to print :"))
for I in range(gh,0,-1):
	kl=str(ji)
	print(kl*I)
	time.sleep(0.1)
print(ji,end="")
for I in range(0,gh):
	kl=str(ji)
	print(kl*I)	
	time.sleep(0.1)
for I in range(gh,0,-1):
	kl=str(ji)
	print(kl*gh)
	time.sleep(0.1)
for I in range(gh,0,-1):
	kl=str(ji)
	print(kl*I)
	time.sleep(0.1)
print(ji,end="")
for I in range(0,gh+1):
	kl=str(ji)
	print(kl*I)
	time.sleep(0.1)
for I in range(gh,0,-1):
	kl=str(ji)
	print(kl*I)
	time.sleep(0.1)
print(ji,end="")
for I in range(0,gh+2):
	kl=str(ji)
	print(kl*I)
	time.sleep(0.1)
	
	