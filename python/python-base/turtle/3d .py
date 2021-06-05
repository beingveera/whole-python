import turtle as t
ts=t.Turtle()
t.bgcolor('black')
t.pensize(2)
t.speed(0.01)
t.color("red","blue")
ts.color("blue","green")
I=1
j=1
for I in range(1,360):
	t.forward(100)
	t.right(90)
	t.left(5)
	t.forward(80)
	t.hideturtle()
	t.goto(0,0)
'''for j in range(1,360):
	ts.bk(80)
	ts.left(90)
	ts.right(10)
	t.bk(100)
	ts.hideturtle()
	ts.goto(100,0)
	'''
	
    