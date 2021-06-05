from random import *
import time

user_pass = int(input("Enter your password length :"))

password =[ '1','2','3','4','5','6','7','8','9','0'
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']

op=['A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']

ps=[ '1','2','3','4','5','6','7','8','9','0']

guess = ""
kl=open("watsaap.txt","w+")
for I in range(1,100):
	   guess=""
	   for letter in range(user_pass):
	       		guess_letter = password[randint(0,55)]
	       		guess = str(guess_letter) + str(guess)
	   print(guess)
	   if guess[0] in op:
	   		if guess[-1] in ps:
	   			kl.write("https://chat.whatsapp.com/{}".format(guess))
	   			kl.write("\n")
 #       		time.sleep(.2)
        		
kl.close()
    		
 