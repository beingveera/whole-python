import re
hand = open('password.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('\S+\S+\d+', line)
	if len(x) > 0:
		print(x)