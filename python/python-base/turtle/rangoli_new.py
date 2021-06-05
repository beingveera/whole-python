import turtle as t
import random as rn
t.color("red")
t.speed(0.01)
for I in range(1,100):
	hl=rn.randint(0,100)
	ps=rn.randint(0,100)
	t.color("blue")
	t.circle(100,steps=6)
	t.color("red")
	t.circle(50)
	t.left(35)
t.exitonclick()
