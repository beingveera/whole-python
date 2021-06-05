from turtle import *

bgcolor("black")
def replace( seq, replacementRules, n ):
    for i in range(n):
        newseq = ""
        for element in seq:
            newseq = newseq + replacementRules.get(element,element)
        seq = newseq
    return seq

def draw( commands, rules ):
    for b in commands:
        try:
            rules[b]()
        except TypeError:
            try:
                draw(rules[b], rules)
            except:
                pass


def main():
    ################################
    # Example 1: Snake kolam
    ################################


    def r():
        color("white")
        right(45)

    def l():
        color("white")
        left(45)

    def f():
        color("white")
        forward(7.5)

    snake_rules = {"-":r, "+":l, "f":f, "b":"f+f+f--f--f+f+f"}
    snake_replacementRules = {"b": "b+f+b--f--b+f+b"}
    snake_start = "b--f--b--f"

    drawing = replace(snake_start, snake_replacementRules, 3)

    reset()
    speed(5)
    tracer(2,0)
    ht()
    up()
    backward(195)
    down()
    draw(drawing, snake_rules)

    from time import sleep
    sleep(3)

    ################################
    # Example 2: Anklets of Veera
    ################################

    def A():
        color("red")
        circle(10,90)

    def B():
        from math import sqrt
        color("black")
        l = 5/sqrt(2)
        forward(l)
        circle(l, 270)
        forward(l)

    def F():
        color("green")
        forward(10)

    Veera_rules = {"a":A, "b":B, "f":F}
    Veera_replacementRules = {"a" : "afbfa", "b" : "afbfbfbfa" }
    Veera_start = "fbfbfbfb"

    reset()
    speed(0)
    tracer(3,0)
    ht()
    left(45)
    drawing = replace(Veera_start, Veera_replacementRules, 3)
    draw(drawing, Veera_rules)
    tracer(1)
    return "Done!"

if __name__=='__main__':
    msg = main()
    print(msg)
    mainloop()
