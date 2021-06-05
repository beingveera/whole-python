import turtle as t
import random as rn
t.color("red")
t.speed(0.01)
for I in range(1,100):
	hl=rn.randint(-200,200)
	ps=rn.randint(-200,200)
#	t.forward(hl)
#	t.bk(70+20)
	t.color("blue")
	t.circle(1)
	t.color("red")
	t.goto(hl,ps)
	t.left(50)
t.exitonclick()
