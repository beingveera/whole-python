from tkinter import *
window=Tk()

expression = ""


def input_number(number, equation):
   global expression
   expression = expression + str(number)
   equation.set(expression)
def clear_input_field(equation):
   global expression
   expression = ""
   equation.set("Enter the Numbers")

def evaluate(equation):
	global expression
	try:
		result = str(eval(expression))
		equation.set(result)
		expression = ""
	except:
		expression = ""

def main():
   equation = StringVar()
   input_field = Entry(window, textvariable=equation)
   input_field.place(height=100)
   input_field.grid(columnspan=4, ipadx=100, ipady=5)
   equation.set("Enter the Numbers")

   _1 = Button(window, text='1', fg='red', bg='yellow', bd=5, command=lambda: input_number(1, equation),width=3)
   _1.grid(row=2, column=0)
   _2 = Button(window, text='2', fg='red', bg='yellow', bd=5, command=lambda: input_number(2, equation),width=3)
   _2.grid(row=2, column=1)
   _3 = Button(window, text='3', fg='red', bg='yellow', bd=5, command=lambda: input_number(3, equation),width=3)
   _3.grid(row=2, column=2)
   _4 = Button(window, text='4', fg='red', bg='yellow', bd=5, command=lambda: input_number(4, equation),width=3)
   _4.grid(row=3, column=0)
   _5 = Button(window, text='5', fg='red', bg='yellow', bd=5, command=lambda: input_number(5, equation),width=3)
   _5.grid(row=3, column=1)
   _6 = Button(window, text='6', fg='red', bg='yellow', bd=5, command=lambda: input_number(6, equation),width=3)
   _6.grid(row=3, column=2)
   _7 = Button(window, text='7', fg='red', bg='yellow', bd=5, command=lambda: input_number(7, equation),width=3)
   _7.grid(row=4, column=0)
   _8 = Button(window, text='8', fg='red', bg='yellow', bd=5, command=lambda: input_number(8, equation),  width=3)
   _8.grid(row=4, column=1)
   _9 = Button(window, text='9', fg='red', bg='yellow', bd=5, command=lambda: input_number(9, equation),width=3)
   _9.grid(row=4, column=2)
   _0 = Button(window, text='0', fg='red', bg='yellow', bd=5, command=lambda: input_number(0, equation), width=3)
   _0.grid(row=5, column=0)
   plus = Button(window, text='+', fg='black', bg='cyan', bd=5, command=lambda: input_number('+', equation),width=3)
   plus.grid(row=2, column=3)
   minus = Button(window, text='-', fg='black', bg='cyan', bd=5, command=lambda: input_number('-', equation),width=3)
   minus.grid(row=3, column=3)
   multiply = Button(window, text='x', fg='black', bg='cyan', bd=5, command=lambda:  input_number('*', equation), width=3)
   multiply.grid(row=4, column=3)
   divide = Button(window, text='/', fg='black', bg='cyan', bd=5, command=lambda: input_number('/', equation), width=3)
   divide.grid(row=5, column=3)
   equal = Button(window, text='=', fg='black', bg='cyan', bd=5, command=lambda: evaluate(equation), width=3)
   equal.grid(row=5, column=2)
   clear = Button(window, text='Clear', fg='black', bg='cyan', bd=5, command=lambda: clear_input_field(equation),width=3)
   clear.grid(row=5, column=1)
   window.mainloop()
   
if __name__ == '__main__':
      main()