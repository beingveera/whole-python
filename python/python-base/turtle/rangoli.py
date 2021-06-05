import turtle as t
import random as rn
t.bgcolor('black')
t.hideturtle()
t.color('red')
t.speed(0.01)
j=rn.randint(1,16)
for I in range(1,25):
	t.circle(80,steps=j)
	t.right(20)
	t.goto(0,0)
	t.write(j)
   