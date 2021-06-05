print("=====================================================")
print("\t\tBINARY CONVERTER")
print("=====================================================")
start=int(input("Enter no. for begin :"))
print("=====================================================")
end=int(input("Enter no. for final :"))
print("=====================================================")
print("Decimal  \t\tBinary")
print("=====================================================")

for num in range(start,end):

	for base in 'db':
		print('{:{width}{base}}'.format(num,base=base, width=start), end='\t\t\t')
	print()					