import re
regex=re.compile('cs[0-9]{4,6}',re.I)
info=input('enter student status:')
tokens=regex.findall(info)
for item in tokens:
	print(item)