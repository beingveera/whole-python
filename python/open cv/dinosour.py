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
    
    lowred=np.array([131,90,106])
    highred=np.array([255,255,255])

    red_mask=cv2.inRange(hsv,lowred,highred)

    contor,hirakey=cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contor=sorted(contor,key=lambda x: cv2.contourArea(x),reverse=True)


    cv2.rectangle(frame,(0,0),(150,150),(0,0,255),2)
    cv2.putText(frame,'JUMP',(40,90),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    for cnt in contor:
        (x,y,w,h)=cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x  +w,y+h),(0,255,0),2)

        if x > 0 and y > 0 and x < 150 and y < 150:
            Press('space') 
            break
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()