'''
from sys import *
import os
import json 
with open("main.json","w") as js :
	for i in range(1,10):
		js.write(str(i))
		js.write("\n")
'''
import json
with open("main.json","r+") as kl:
    hj=kl.read()
    print(hj[0])
    for i in range(1,10):
        print(hj[16])
	        