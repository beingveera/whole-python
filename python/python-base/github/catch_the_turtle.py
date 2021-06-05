from turtle import *
import time 
import random as rn 

bgcolor("black")

t1=Turtle()
t1.shape("turtle")
t2=Turtle()
t2.shape("turtle")
t3=Turtle()


count=0
t2.hideturtle()

t1.color("red")


for I in range(1,20):
	y=rn.randint(-400,400)
	x=rn.randint(-270,270)
	si=rn.randint(1,180)
	
	t2.shapesize(2)
	t2.color("white")
	t2.penup()
	t2.goto(x,y)
	t1.shapesize(2)
	t1.left(si)
	t1.penup()
	t1.goto(x,y)
	t1.pendown()
	t2.hideturtle()
	t2.penup()
	
	
	
	
	
	t3.shapesize(.1)
	t3.hideturtle()
	t3.penup()
	t3.color("yellow")
	t3.goto(200,200)	
	t3.pendown()
	count+=1
	t3.width(5)
	t3.write(I)
	time.sleep(1)
	t2.reset()
	t3.reset()
	
	

	
	





exitonclick()