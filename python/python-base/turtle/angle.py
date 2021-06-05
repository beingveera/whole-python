from turtle import *
import time
for angle in range(0, 360, 20):
      setheading(angle)
      forward(170)
      write(str(angle) + '*')
      backward(170)
      time.sleep(0.1)
quit()