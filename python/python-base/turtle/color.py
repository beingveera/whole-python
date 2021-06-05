from turtle import *
colors = ['blue','pink','red','green','yellow']
for x in range(200):
     pencolor(colors[x % 5])
     width(x/10 + 1)
     forward(x)
     left(60)
quit()