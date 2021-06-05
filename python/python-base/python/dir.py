import numpy as np
import json
j=1
with open("num.txt","w") as pl:
	for i in dir(np):
		print(i)
		pl.write("{} The module function : {}".format(j,i))
		j=j+1
		pl.write("\n")
		