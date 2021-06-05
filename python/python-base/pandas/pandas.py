import pandas
j=1
with open("pandas.txt","w") as df:
	for I in dir(pandas):
		df.write("{}. function : {}".format(j,I))
		for k in dir(pandas ".{}".format(I)):
		j+=1
		df.write("\n")
	