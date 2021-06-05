import cv2 
import math

path='one.jpg'
img=cv2.imread(path)
points=[]
def mouse(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(0,0,255),cv2.FILLED)
        points.append([x,y])
        print(points)

def getAngle():
    print("Angle : ")
while True:

    if len(points) %3 :
        getAngle()

    cv2.imshow('frame',img)
    cv2.setMouseCallback('frame',mouse)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        points = []
        img=cv2.imread(path)