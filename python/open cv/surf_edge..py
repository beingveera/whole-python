import numpy as np 
import cv2 
import imutils
import pyautogui

def Press(key):
    pyautogui.press(key)

cap=cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    frame=cv2.flip(frame,1) 
    frame=imutils.resize(frame,height= 600,width=600)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lowred=np.array([140,90,130])
    highred=np.array([255,255,255]) 
    red_mask=cv2.inRange(hsv,lowred,highred)

    contor,hirakey=cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contor=sorted(contor,key=lambda x: cv2.contourArea(x),reverse=True)


    cv2.rectangle(frame,(240,0),(340,100),(0,0,255),2)
    cv2.putText(frame,'Start',(250 ,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.rectangle(frame,(0,200),(100 ,300),(0,0,255),2)
    cv2.putText(frame,'Left',(10 ,260),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.rectangle(frame,(500,200),(599,300),(0,0,255),2)
    cv2.putText(frame,'Right',(520,260),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    for cnt in contor:
        (x,y,w,h)=cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x  +w,y+h),(0,255,0),2)

        if x > 240 and y > 0 and x < 340 and y < 100:
            Press('space') 
            break
        if x > 0 and y > 100 and x < 200 and y < 300:
            Press('a') 
            break
        if x > 500 and y > 200 and x < 600 and y < 300:
            Press('d') 
            break
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()