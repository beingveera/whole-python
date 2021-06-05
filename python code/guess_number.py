'''
import random as rn 
import numpy as np 
ins=np.random.randint(1,10)
print(ins)
i=0
k=0
for i in range(3,0,-1):
    print('\nRemaining Chances : {}'.format(i))
    out=int(input('\nEnter the Guess Number : '))
    if out == ins:
        print('\nYou are Win the game...')
        k+=1
        break
    if i == 0 and k == 0:
        print('\nYou Lost The Game...')
        break   
'''
import numpy as np 
class game:
    def __init__(self):
        self.ins=np.random.randint(1,10)
        self.i=0
        self.k = 0
    def main(self):
        for self.i in range(3,0,-1):
            print('\nRemaining Chances is : {} '.format(self.i))
            self.out= int(input("Enter the guess Number : "))
            if self.out == self.ins:
                print('You Win The Game ....')
                self.k+=24
                break
            if self.i == 1:
                print('You Lost the Game...')  
                break
            elif self.out > self.ins:
                print('Guess Number is Gratter then the OutPut ....')
            if self.i == 1:
                print('You Lost the Game...')
            elif self.out < self.ins :
                print('Guess Number is Lower then the OutPut ...')  
gamer1=game()
gamer1.main()
        
    
