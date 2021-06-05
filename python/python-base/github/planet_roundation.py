
from turtle import Shape, Turtle, mainloop, Vec2D as Vec
import turtle
import time


turtle.bgcolor("black")

ls=Turtle()
ls.color("cyan")
ls.hideturtle()
ls.penup()
ls.goto(-140,320)
ls.write("Universe Sun Moon Orbit")

time.sleep(1)

ls.clear()



G = 8

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        for i in range(10000):
            self.t += self.dt
            for p in self.planets:
                p.step()

class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape=shape)
        self.penup()
        self.m = m
        self.setpos(x)
        self.v = v
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.resizemode("user")
        self.pendown()
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5*dt*self.a
    def acc(self):
        a = Vec(0,0)
        for planet in self.gravSys.planets:
            if planet != self:
                v = planet.pos()-self.pos()
                a += (G*planet.m/abs(v)**3)*v
        return a
    def step(self):
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt*self.v)
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        self.v = self.v + dt*self.a


def main():
    s = Turtle()
    s.reset()
    s.getscreen().tracer(0,0)
    s.ht()
    s.pu()
    s.fd(6)
    s.lt(90)
    s.begin_poly()
    s.circle(6, 180)
    s.end_poly()
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(6,180)
    s.end_poly()
    m2 = s.get_poly()

    planetshape = Shape("compound")
    planetshape.addcomponent(m1,"red")
    planetshape.addcomponent(m2,"blue")
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(1,0)

    gs = GravSys()
    sun = Star(1000000, Vec(0,0), Vec(0,-2.5), gs, "circle")
    sun.color("yellow")
    ls.penup()
    ls.goto(0,-50)
    ls.pendown()
    ls.write("Sun")
    sun.shapesize(1.8)
    sun.pu()
    earth = Star(12500, Vec(210,0), Vec(0,195), gs, "planet")
    earth.pencolor("red")
    earth.shapesize(1.7)
    moon = Star(1, Vec(220,0), Vec(0,295), gs, "planet")
    moon.pencolor("blue")
    moon.shapesize(1)
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
