import random as rn
import time as tm
x=2
while True:
    nm=rn.randint(1,10)
    if nm == 11:
    	break
    tm.sleep(x)
    x=x-0.1
    print(nm)
