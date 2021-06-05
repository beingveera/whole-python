import re
hand = open('password.txt',"r")
for line in hand:
	line = line.strip()
	if re.search('is', line):
		print(line)