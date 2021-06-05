import emoji
ln=int(input("Enter the length :"))
for i in range(1,ln+1):
	l=emoji.emojize(":red_heart:")
	print(l*i)