import turtle as t
import random as rn
t.color("red")
t.speed(0.01)
for I in range(1,200):
	hl=rn.randint(0,70)
	t.color("blue")
	t.circle(hl)
	t.color("red")
	t.circle(hl-10)
	t.left(180)
t.exitonclick()
