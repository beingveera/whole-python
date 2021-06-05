import turtle as t
ts=t.Turtle()
t.bgcolor("black")
ts.speed(0)
colors=["red","blue","green","yellow"]
for I in range(0,1000):
	ts.color(colors[I % 4])
	ts.forward(100)
	ts.left(45)
	ts.forward(150)
	ts.goto(0,0)
	ts.left(10)