from sys import *
import os
import json 
with open("os.json","w") as js :
	for i in dir(os):
		js.write(i)
		js.write("\n")
		