import turtle as t
import random as rn
ts=t.Turtle()
ts1=t.Turtle()
t.bgcolor('black')
ts.shape("turtle")
ts1.shape('turtle')
ts.color('red','blue')
ts1.color('blue','red')
ts.speed(0.01)
colors=['red','green','blue','yellow','pink','white','purple','orange','gold','grey']
for I in range(1,1000):
	i=rn.randint(0,100)
	ts.color(colors[I%10])
	ts.circle(70,steps=7)
	ts.goto(i,i+10)
	ts1.hideturtle()
	ts.hideturtle()