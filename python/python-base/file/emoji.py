import emoji
with open("emoji.txt","w") as df:
	ls=emoji.UNICODE_EMOJI
	for I in ls:
		ps=emoji.demojize(I)
		df.write(" {}  >>>  {} ".format(I,ps))
		df.write("\n")