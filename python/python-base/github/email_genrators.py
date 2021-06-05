import random as rn
import json


names=[

'Acharya', 'Agarwal', 'Agate','Aggarwal', 'Agrawal', 'Ahluwalia', 'Ahuja', 'Amble', 'Anand', 'Andra', 'Anne', 'Apte', 'Arora', 'Arya', 'Atwal','Aurora', 'Babu','Badal','Badami', 'Bahl', 'Bahri', 'Bail', 'Bains', 'Bajaj', 'Bajwa', 'Bakshi', 'Bal',  'Bala',
 'Balu','Balakrishnan', 'Balan','Balasubramanian', 'Balay','Bali', 'Bandi', 'Banerjee', 'Banik', 'Bansal', 'Barad', 'Barad', 'Baral', 'Baria', 'Barman', 'Basak','Bassi', 'Basu','Bath', 'Batra','Batta','Bava', 'Bawa',
 'Bedi', 'Behl', 'Ben', 'Bera','Bhagat', 'Bhakta', 'Bhalla', 'Bhandari', 'Bhardwaj', 'Bhargava', 'Bhasin', 'Bhat',
 'Bhatia', 'Bhatnagar', 'Bhatt', 'Bhattacharyya', 'Bhatti', 'Bhavsar', 'Bir', 'Biswas', 'Boase', 'Bobal', 'Bora', 'Bora', 'Borah', 'Borde', 'Borra', 'Bose', 'Brahmbhatt', 'Brar', 'Buch', 'Buch', 'Bumb', 'Butala', 'Chacko', 'Chad', 'Chada', 'Chadha', 'Chahal','Chakrabarti', 'Chakraborty', 'Chana',
 'Chand', 'Chanda', 'Chander','Chandra', 'Chandran', 'Char', 'Chatterjee', 'Pagination', 'Chaudhari', 'Chaudhary', 'Chaudhry', 'Chaudhuri', 'Chaudry', 'Chauhan', 'Chawla', 'Cheema', 'Cherian', 'Chhabra', 'Chokshi', 'Chopra', 'Choudhary',
 'Choudhry', 'Choudhury', 'Chinki','Comar', 'Contractor', 'D’Alia', 'Dada', 'Dalal', 'Dani', 'Dar', 'Dharm', 'Dara', 'Das', 'Dasgupta', 'Dash', 'Dass', 'Date',
 'Datta', 'Dave', 'Dayal', 'Deeapk','Deep', 'Deo', 'Deol', 'Desai', 'Deshmukh', 'Deshpande', 'Devan', 'Devi', 'Dewan',
 'Dey', 'Dhaliwal', 'Dhar', 'Dhar','Dhawan', 'Dhillon','Dhingra', 'Din', 'Divan','Dixit', 'Doctor', 'Dora', 'Doshi','Dua', 'Dube', 'Dubey', 'Dugal', 'Dugar', 'Dugar', 'Dutt', 'Dutta','Dyal', 'Edwin','Gaba',  'Gade', 'Gala','Gandhi','Ganesan', 'Ganesh', 'Ganguly', 'Gara', 'Garde', 'Garg', 'Gera', 'Ghose', 'Ghosh','Gill', 'Goda', 'Goel', 'Gokhale', 'Gola', 'Gole', 'Golla', 'Gopal', 'Goswami','Gour', 'Goyal', 'Grewal', 'Grover',
 'Guha', 'Gulati', 'Gupta', 'Halder', 'Handa', 'Hans', 'Hari', 'Hayre','Hegde', 
 'Hora', 'Issac', 'Iyengar', 'Iyer', 'Jaggi', 'Jain','Jani', 'Jayaraman','Jha', 'Jhaveri', 'Johal', 'Joshi',  'Kadakia', 'Kade', 'Kakar', 'Kola', 'Kalle', 'Kalu', 'Kale','Kalita', 'Kalla', 'Kamdar', 'Kanda'
 'Kannan', 'Kant','Kapadia', 'Kapoor',
 'Kapur', 'Kar', 'Kara', 'Karan', 'Kari', 'Karnik', 'Karpe', 'Kashyap', 'Kata', 'Kaul', 'Kaur', 'Keer', 'Keer', 'Khalsa',
 'Khanna', 'Khare', 'Khatri',  'Khosla', 'Khurana', 'Kibe', 'Kohli', 'Konda', 'Korpal', 'Koshy', 'Kota', 'Kothari', 'Krish', 'Krishna', 'Krishnamurthy', 'Krishnan', 'Kulkarni', 'Kumar', 'Kumer', 'Kunda', 'Kurian', 'Kuruvilla', 'Lad', 'Lalu', 'Lal', 'Lala', 'Lall', 'Lalla', 'Lanka',
 'Lata', 'Loke', 'Loyal', 'Luthra', 'Madan', 'Madan', 'Magar', 'Mahajan', 'Mahal', 'Maharaj', 'Majumdar''Malhotra', 'Mall', 'Mallick', 'Mammen', 'Mand', 'Manda','Mandal', 'Mander', 'Mane', 'Mangal', 'Mangat', 'Mani','Manu', 'Mann', 'Mannan','Manne', 'Master', 'Raj', 'Raja', 'Rajagopal', 'Rajagopalan', 'Rajan', 'Raju', 'Ram', 'Rama', 'Ramachandran', 'Ramakrishnan', 'Raman', 'Ramanathan', 'Ramaswamy', 'Ramesh', 'Rana', 'Randhawa', 'Ranganathan', 'Rao','Rastogi', 'Ratta', 'Rattan', 'Ratti', 'Rau', 'Raval', 'Ravel', 'Ravi', 'Ray', 'Reddy', 'Rege', 'Rout', 'Roy', 'Sabharwal', 'Sacha','Sachdev', 'Sachdeva', 'Sagar', 'Saha', 'Sahni', 'Sahota', 'Saini', 'Salvi', 'Sama', 'Sami', 'Sampath', 'Samra',
 'Sandal', 'Sandhu', 'Sane', 'Sangha','Sanghvi', 'Sani', 'Sankar', 'Sankaran','Sant', 'Saraf', 'Saran', 'Sarin', 'Sarkar', 'Sarma', 'Sarna', 'Sarraf', 'Sastry', 'Sathe', 'Savant', 'Sawhney', 'Saxena', 'Sehgal', 'Sekhon', 'Sem', 'Sen', 'Sengupta', 'Seshadri', 'Seth', 'Sethi', 'Setty', 'Sha', 'Shah', 'Shan', 'Shankar', 'Shanker', 'Sharaf', 'Sharma',  'Shenoy', 'Shere', 'Sheth', 'Shetty', 'Shroff','Shukla',  'Sibal', 'Sidhu', 'Singh','Singhal''Sinha', 'Sodhi', 'Solanki', 'Som', 'Soman', 'Soni', 'Sood', 'Raj',  'Raja', 'Rajagopal', 'Rajagopalan', 'Rajan', 'Raju', 'Ram', 'Rama', 'Ramachandran','Ramakrishnan', 'Raman', 'Ramanathan', 'Ramaswamy','Ramesh', 'Rana', 'Randhawa', 'Ranganathan', 'Rao', 'Rastogi', 'Ratta', 'Rattan', 'Ratti', 'Rau', 'Raval', 'Ravel',  'Ravi', 'Ray', 'Reddy', 'Rege', 'Rout', 'Roy', 'Sabharwa', 'Sachar', 'Sachde', 'Sachdeva', 'Sagar', 'Saha', 'Sahni', 'Sahota', 'Saini', 'Salvi', 'Sama', 'Sami', 'Sampath','Samra', 'Sandal', 'Sandhu', 'Sane',  'Sangha', 'Sanghvi', 'Sani', 'Sankar', 'Sankaran', 'Sant', 'Saraf', 'Saran', 'Sarin', 'Sarkar', 'Sarma', 'Sarna', 'Sarraf', 'Sastry', 'Sathe', 'Savant', 'Sawhney','Saxena', 'Sehgal', 'Sekhon', 'Sem', 'Sen', 'Sengupta', 'Seshadri', 'Seth', 'Sethi', 'Setty', 'Sha', 'Shah', 'Shan', 'Shankar', 'Shanker', 'Sharaf', 'Sharma', 'Shenoy' 'Shere','Sheth','Shetty','Shroff','Shukla', 'Sibal', 'Sidhu', 'Singh', 'Singhal', 'Sinha', 'Sodhi','Solanki', 'Som', 'Soman','Lokesh', 'Techno', 'Veera'
 
 ]

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]

letters = ["1","2","3","4","5","6","7","8","9","0"]

add=""

print("=====================================================")
print("\t\tEmail Generator ")
print("=====================================================\n")

ch=int(input("No. of Emails :"))

print("=====================================================\n")

email= ""

k=0

with open("emails.json","w") as lp:
	while k!= ch :	
		nm=rn.randint(0,497)
		email_name=names[nm]
	
		for I in range(1,5):
			no1=rn.randint(1, 9)
			no2=rn.randint(1, 9)
			no3=rn.randint(1, 9)
			no4=rn.randint(1, 9)
			
			a=letters[no1]
			b=letters[no2]
			c=letters[no3]
			d=letters[no4]
			add=a+b+c+d		
		
		dom=rn.randint(0,5)
		back=domains[dom]
	
		ld=email_name+add+ "@"+back
#	print("{}{}@{}".format(email_name,add,back))
		#lp.load("Email :  {}  ".format(ld))
		lp.write("Email  {} :  {}".format(k+1,ld))
		lp.write("\n")
		print("====================",end="")
		print("====================",end="")
		print("============")
		
		print(ld)
			
		k+=1

	
	

