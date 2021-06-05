'''
created by Lokesh Sharma 
Geetanjali institute of technical studies, Udaipur

'''
from tkinter import *

root = Tk()
root.geometry('330x370')
  
class data_predictor():

    def __init__(self):
        self.setZero()
        self.solve()
        
    
    def setZero(self):
        for i in range(9):
            for j in range(9):
                if filledBoard[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    filledBoard[i][j].set(0)


    def solve(self):
        findEmpty = self.emptyCell()
        
        if not findEmpty:
            return True   
        else:
            row, column = findEmpty
        
        for i in range(1,10):
            if self.isValid(i, (row, column)):
                filledBoard[row][column].set(i)

                if self.solve():
                    return True

                filledBoard[row][column].set(0)
        
        return False
 
    def isValid (self, num, pos):
        
        for i in range(9):
            if filledBoard[pos[0]][i].get() == str(num):
                return False
      

        for i in range(9):
            if filledBoard[i][pos[1]].get() == str(num):
                return False

        row = pos[0] // 3 
        column = pos[1] // 3 

        for i in range(row * 3, (row * 3) + 3):
            for j in range(column * 3, (column * 3) + 3):
                if filledBoard[i][j].get() == str(num):
                    return False 
        return True


    def emptyCell(self):
        for row in range(9):
            for column in range(9):
                if filledBoard[row][column].get() == '0':
                    return (row,column)
        return None


class Interface():
    def __init__(self, window):
        self.window = window
        window.title("Sudoku Data Predictor")

        font = ('Arial', 20)
        color = 'white'

        solve = Button(window, text = 'Solve', command = self.Solve,bg="yellow")
        solve.grid(column=3,row=20)
        clear = Button(window, text = 'Clear', command = self.Clear,bg="yellow")
        clear.grid(column = 5,row=20)

        self.board  = []
        for row in range(9):
            self.board += [["","","","","","","","",""]]

        for row in range(9):
            for col in range(9):
                if (row < 3 or row > 5) and (col < 3 or col > 5):
                    color = 'gray' 
                elif (row >= 3 and row < 6) and (col >=3 and col < 6):
                    color = 'gray'
                else:
                    color = 'white'   
            
                self.board[row][col] = Entry(window, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 2,
                                          highlightcolor = 'yellow', highlightthickness = 0, highlightbackground = 'black', 
                                          textvariable = filledBoard[row][col]) 
                self.board[row][col].bind('<FocusIn>', self.gridChecker) 
                self.board[row][col].bind('<Motion>', self.gridChecker)                        
                self.board[row][col].grid(row = row, column = col)


    def gridChecker(self, event):
        for row in range(9):
            for col in range(9):
                if filledBoard[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    filledBoard[row][col].set('')

    def Solve(self):
        data_predictor()

    def Clear(self):
        for row in range(9):
            for col in range(9):
                filledBoard[row][col].set('')

filledBoard = []
for row in range(9): 
    filledBoard += [["","","","","","","","",""]]
for row in range(9):
    for col in range(9):
        filledBoard[row][col] = StringVar(root)    

Interface(root)
root.mainloop()



