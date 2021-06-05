from turtle import * 
import random as rn
bgcolor("black")
x=1
speed(0)
shape("turtle")
while x <400:
	r=rn.randint(0,255)
	g=rn.randint(0,255)
	b=rn.randint(0,255)
	colormode(255)
	pencolor( r,g,b)
	forward(5+x)
	right(909)
	x=x+1
exitonclick()
	