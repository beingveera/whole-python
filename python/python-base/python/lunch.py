famt1=0
famt2=0
famt3=0
famt4=0
famt5=0
famt6=0
con1=0
con2=0
con3=0
con4=0
con5=0
con6=0
while(1):
   print('\t\t1.Roti')
   print('\t\t2.Rice')
   print('\t\t3.Butter Milk')
   print('\t\t4.Dal Makhni')
   print('\t\t5.Salad')
   print('\t\t6.Green Veg')
   print('\t\t7.Bill')
   ch=int(input('\t\tenter your choice:'))
   if ch is 1:
   	quan1=int(input('enter quan:'))
   	famt1=quan1*10
   	con1=quan1+con1
   elif ch is 2:
   	quan2=int(input('enter quan:'))
   	famt2=quan2*25
   	con2=quan2+con2
   elif ch is 3:
   	quan3=int(input('enter quan:'))
   	famt3=quan3*10
   	con3=quan3+con3
   elif ch is 4:
   	quan4=int(input('enter quan:'))
   	famt4=quan4*50
   	con4=quan4+con4
   elif ch is 5:
   	quan5=int(input('enter quan:'))
   	famt5=quan5*15
   	con5=quan5+con5
   elif ch is 6:
   	quan6=int(input('enter quan:'))
   	famt6=quan6*40
   	con6=quan6+con6
   elif ch is 7:
       tot=famt1+famt2+famt3+famt4+famt5+famt6     
       print('\nyour total bill is : ' ,tot ,'rupees',"\n")
       print('Total Roti :',con1)
       print('Total plate Rice :',con2)
       print("Total glass of butter milk :",con3)
       print("Total bowl of dal makhni :",con4)
       print('Total plate of salad :',con5)
       print('Total bowl of green veg :',con6)
       print('\nyour total bill is : ' ,tot ,'rupees',"\n")
 