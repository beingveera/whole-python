import cv2
import numpy as np
import os 
import time 
from win10toast import ToastNotifier
import pyttsx3

cap=cv2.VideoCapture(0)

notifier=ToastNotifier()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


try: 
    if not os.path.exists('codethon'): 
        os.makedirs('codethon') 
except OSError: 
    print ('Error: Creating directory of codethon') 
  
currentframe = 0

while cap.isOpened():
    _,img=cap.read()
    ret,frame1=cap.read()
    ret,frame2=cap.read()

    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)

    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)<10:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame1,'status: {}'.format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
            notifier.show_toast("Alert","Motion is found....",threaded=True,icon_path=None)
            engine.say("Motion is Found ...")
            engine.runAndWait()
                               
      
            name = './codethon/detection_' + str(currentframe) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, img) 
            currentframe += 1
            time.sleep(0.5)
            continue
        

       #cv2.drawContours(frame1,contours,-1,(255,255,0),2)
    cv2.imshow('feed',frame1)
    cv2.imshow('gray',gray)
    cv2.imshow('blur',blur)
    cv2.imshow('threshold',thresh)
    frame1=frame2
    ret,frame2=cap.read()
    
    if cv2.waitKey(10)==27:
        break
cv2.destroyAllWindows()
cap.release()

