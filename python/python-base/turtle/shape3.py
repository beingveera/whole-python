import turtle as t
import random as rn
t.color("red")
t.speed(0.01)
for I in range(1,200):
	hl=rn.randint(0,70)
	t.color("red")
	t.circle(hl,steps=6)
	t.color("blue")
	t.circle(hl+10,steps=6)
	t.left(90)
t.exitonclick()
