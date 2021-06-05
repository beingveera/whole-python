from covid import Covid
obj=Covid()



print("-----------------------------------------------------")
print("\t\tcovid data plotter")
print("-----------------------------------------------------\n")

while True:
	print("1.data of all countries.")
	print("2.data by name.")
	print('3.data by Id.')
	print("4.total Active cases ")
	print("5.total confirm cases ")
	print("6.total recover cases")
	print("7.total death")
	print("8.Exit")
	print("-----------------------------------------------------\n")
	
	op=int(input("Enter your Choice :"))
	print("\n")
	if op == 1:
		lk=obj.get_data()
		for I in lk:
			print(I,end="\n\n")
		print("\n")
		
	elif op == 2 :
		nm=input("Enter the Country Name :")
		lm=obj.get_status_by_country_name(nm)
		for x in lm:
			print(x, " : ",lm[x])
		print("-----------------------------------------------------\n")
		
	elif op == 3:
		val=int(input("Enter the Country id :"))
		bn=obj.get_status_by_country_id(val)
		for x in bn:
			print(x, " : ",bn[x])
		print("-----------------------------------------------------\n")
		
	elif op == 4:
		wol=obj.get_total_active_cases()
		print("The  total Active Cases in the world is : {}".format(wol))
		print("-----------------------------------------------------\n")
		
	elif op == 5:
		wole=obj.get_total_confirmed_cases()
		print("The total Confirmed Cases in the world is : {}".format(wole))
		print("-----------------------------------------------------\n")
		
	elif op == 6:
		reco=obj.get_total_recovered()
		print("The total Recovered Cases in the world is : {}".format(reco))
		print("-----------------------------------------------------\n")
	
	elif op == 7:
		deth=obj.get_total_deaths()
		print("The total deaths in the world is : {}".format(deth))
		print("-----------------------------------------------------\n")
		
	elif op == 8 :
		exit()
		
	
		
			
		
		
