import turtle as t
t.color("red")
t.hideturtle()
t.width(5)
#t.speed(0.01)
t.penup()
t.goto(-233,404)
t.pendown()
for i in range(1,5):
	t.forward(464)
	t.right(90)
	t.forward(804)
	t.right(90)
else:
	t.goto(0,0)
	for I in range(1,100):
		t.circle(45,steps=5)
t.exitonclick()

	