

import turtle
import time
import random
import numpy

delay=0.1
score=0

win=turtle.Screen()
win.bgcolor('pink')
win.setup(width=600,height=600)
win.tracer(0)

color=['red','blue','green','yellow','black','brown','white','purple','skyblue','orange']

game=turtle.Turtle()
game.hideturtle()
game.penup()
game.goto(0,0)
game.write(" <<< Game Start >>>  ",align='center' , font={'Courier',300,'normal'})
time.sleep(0.5)
game.clear()


cl=random.randint(0,9)
car=turtle.Turtle()
car.shape('square')
car.left(90)
car.speed(0)
car.color(color[cl])
car.penup()
car.goto(0,-260)
car.direction ='right'

ps=[]
for i in range(65,80):
    obj=chr(i)
    obj=turtle.Turtle()
    ps.append(obj)
print(type(obj))
x=numpy.random.randint(-290,290,len(ps)-1)
for i in range (len(ps)-1):
    ps[i].shape('circle')
    ps[i].speed(0)
    div=random.randint(0,9)
    ps[i].color(color[div])
    ps[i].penup()
    ps[i].right(90)
    ps[i].goto(x[i],290)
ps[len(ps)-1].hideturtle()
ps[len(ps)-1].penup()

pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("  \t\tScore : 0  \t\t  ", align='center' , font={'Courier',50,'normal'})


def obj_move():
    x=numpy.random.randint(1,50,len(ps)-1)
    for i in range(len(ps)-1):
        ps[i].forward(x[i])
        time.sleep(0)
        
def movement():
    if car.direction== 'left':
        x=car.xcor()
        car.setx(x+20)
    
    if car.direction== 'right':
        x=car.xcor()
        car.setx(x-20)

def move_left():
    car.direction= 'left'
def move_right():
    car.direction = 'right'

win.listen()
win.onkeypress(move_left,'m')
win.onkeypress(move_right,'n')

while True:
    win.update()

    if car.xcor()>290 or car.xcor()< -290:
        time.sleep(1)
        car.goto(0,-260)

    movement()
    time.sleep(delay)

    obj_move()

    x=numpy.random.randint(-290,290,len(ps)-1)
    k=1
    for i in range(len(ps)-1):
        if car.distance(ps[i])< 40:
            ps[i].goto(x[i-3],290)
            ps[i-1].goto(x[i-5],290)
            ps[i-2].goto(x[i-7],290)
            ps[i-3].goto(x[i-10],290)
            ps[i-4].goto(x[i-13],290)
            if score < 300:
                car.shapesize(0.5)
            elif score > 300 and 500 > score:
                car.shapesize(1) 

            car.shapesize(3)
            score+=10
            pen.clear()
            pen.write("\t\t  Score : {}  \t\t  ".format(score), align='center',font={'Courier',50,'normal'})

    print(car.pos())

turtle.mainloop()