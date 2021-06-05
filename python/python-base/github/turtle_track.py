from turtle import *

def switchupdown(x=0, y=0):
    if pen()["pendown"]:
        end_fill()
        up()
    else:
        down()
        begin_fill()

def changecolor(x=0, y=0):
    global colors
    colors = colors[1:]+colors[:1]
    color(colors[0])

def main():
    global colors
    shape("turtle")
    resizemode("user")
    shapesize(1)
    width(3)
    colors=["red", "green", "blue", "yellow","cyan","purple","black"]
    color(colors[0])
    switchupdown()
    onscreenclick(goto,1)
    onscreenclick(changecolor,2)
    onscreenclick(switchupdown,3)

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
