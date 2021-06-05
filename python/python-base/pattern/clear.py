from subprocess import call
import os
from time import sleep 
def clear(): 
    _ = call('clear' if os.name =='posix' else 'cls') 
sleep(1) 
for i in range(1,10,2):
	print(" "*i)
	print("*",end=" ")
	clear()
	