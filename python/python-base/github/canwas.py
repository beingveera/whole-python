from turtle import TurtleScreen, RawTurtle, TK

import random as rn

import turtle 
turtle.bgcolor("black")
def main():
    root = TK.Tk()
    cv1 = TK.Canvas(root, width=500, height=400, bg="red")
    cv2 = TK.Canvas(root, width=500, height=400, bg="blue")
    cv1.pack()
    cv2.pack()

    s1 = TurtleScreen(cv1)
    s1.bgcolor(0,0,0)
    s2 = TurtleScreen(cv2)
    s2.bgcolor(1,1,1)

    p = RawTurtle(s1)
    q = RawTurtle(s2)

    p.color("red", (1,1,1))
    p.width(2)
    q.color("blue", (0,0,0))
    q.width(2)
    
    ls=rn.randint(1,15)
    kl=rn.randint(30,90)

    for t in p,q:
        t.shape("turtle")
        t.shapesize(1)
        t.lt(90)

    q.lt(90)

    for t in p, q:
        t.begin_fill()
    for i in range(1,4):
        for t in p, q:
          for I in range(1,5):
            	t.circle(50,steps=ls)      
            	t.lt(30)     
    for t in p,q:
        t.end_fill()
        t.lt(50)
        t.pu()
        t.bk(140)



if __name__ == '__main__':
    main()
    TK.mainloop()  
