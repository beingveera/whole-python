import turtle as t
t.color("red","blue")
t.begin_fill()
for I in range(1,10):
	t.forward(90)
	t.left(45)
	t.goto(0,0)
	t.forward(90)
	t.left(90)
t.end_fill()