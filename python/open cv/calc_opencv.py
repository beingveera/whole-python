

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
    frame=imutils.resize(frame,height= 200,width= 800)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lowred=np.array([140,90,130])
    highred=np.array([255,255,255]) 
    red_mask=cv2.inRange(hsv,lowred,highred)

    contor,hirakey=cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contor=sorted(contor,key=lambda x: cv2.contourArea(x),reverse=True)


    cv2.rectangle(frame,(0,0),(100,100),(0,0,255),2)
    cv2.putText(frame,'1',(40,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(0,100),(100,200),(0,0,255),2)
    cv2.putText(frame,'3',(40,160),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(0,200),(100,300),(0,0,255),2)
    cv2.putText(frame,'5',(40,260),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(0,300),(100,400),(0,0,255),2) 
    cv2.putText(frame,'7',(40,360),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(0,400),(100,500),(0,0,255),2)
    cv2.putText(frame,'9',(40,460),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
   
    
    cv2.rectangle(frame,(100,0),(200,100),(0,0,255),2)
    cv2.putText(frame,'2',(140,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(100,100),(200,200),(0,0,255),2)
    cv2.putText(frame,'4',(140,160),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(100,200),(200,300),(0,0,255),2)
    cv2.putText(frame,'6',(140,260),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(100,300),(200,400),(0,0,255),2)
    cv2.putText(frame,'8',(140,360),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(100,400),(200,500),(0,0,255),2)
    cv2.putText(frame,'0',(140,460),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(100,500),(200,600),(0,0,255),2)
    cv2.putText(frame,'Back',(10,460),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    
    
     
    cv2.rectangle(frame,(800,0),(700,100),(0,0,255),2)
    cv2.putText(frame,'+',(740,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(800,100),(700,200),(0,0,255),2)
    cv2.putText(frame,'-',(740,160),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(800,200),(700,300),(0,0,255),2)
    cv2.putText(frame,'*',(740,260),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(800,300),(700,400),(0,0,255),2)
    cv2.putText(frame,'/',(740,360),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(800,400),(700,500),(0,0,255),2)
    cv2.putText(frame,'=',(740,460),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.rectangle(frame,(800,500),(700,600),(0,0,255),2)
    cv2.putText(frame,'Clear',(720,560),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
   
   
 
   

    for cnt in contor:
        (x,y,w,h)=cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x  +w,y+h),(0,255,0),2)

        if x > 0 and y > 0 and x < 100 and y < 100:
            Press('1') 
            break
        elif x > 0 and y > 100 and x < 100 and y < 200:
            Press('3') 
            break
        elif x > 0 and y > 200 and x < 100 and y < 300:
            Press('5') 
            break
        elif x > 0 and y > 300 and x < 100 and y < 400:
            Press('7') 
            break
        elif x > 0 and y > 400 and x < 100 and y < 500:
            Press('9') 
            break
        
        elif x > 100 and y > 0 and x < 200 and y < 100:
            Press('2') 
            break
        elif x > 100 and y > 100 and x < 200 and y < 200:
            Press('4') 
            break
        elif x > 100 and y > 200 and x < 200 and y < 300:
            Press('6') 
            break
        elif x > 100 and y > 300 and x < 200 and y < 400:
            Press('8') 
            break
        elif x > 100 and y > 400 and x < 200 and y < 500:
            Press('0') 
            break
        elif x > 100 and y > 500 and x < 200 and y < 600:
            Press('backspace') 
            break
        
        elif x > 700 and y > 0 and x < 800 and y < 100:
            Press('+') 
            break
        elif x > 700 and y > 100 and x < 800 and y < 200:
            Press('-') 
            break
        elif x > 700 and y > 200 and x < 800 and y < 300:
            Press('*') 
            break
        elif x > 700 and y > 300 and x < 800 and y < 400:
            Press('/') 
            break
        elif x > 700 and y > 400 and x < 800 and y < 500:
            Press('=') 
            break
        elif x > 700 and y > 500 and x < 800 and y < 600:
            Press('esc') 
            break
        
        
        
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break  
cap.release()
