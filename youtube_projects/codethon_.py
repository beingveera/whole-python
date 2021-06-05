import cv2
import numpy as np
import os 
import time 
from win10toast import ToastNotifier
import pyttsx3
import matplotlib.pyplot as plt
import random
import urllib.request
import requests
import threading
import json

colors=['red','blue','yellow','green','black','gray','purple','orange','brown']
ls=[]
ps=[]
lis_1=[] 
lis_2=[] 
lis_3=[]

URl='https://api.thingspeak.com/update?api_key=U3NYBUOI9R9QF58V&field1=0'
KEY='U3NYBUOI9R9QF58V'

    

cap=cv2.VideoCapture(0)

notifier=ToastNotifier()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

try: 
    if not os.path.exists('codethon'): 
        os.makedirs('codethon')
    if not os.path.exists('codethon_videos'): 
        os.makedirs('codethon_vidoes')
    
except OSError: 
    print ('Error: Creating directory of codethon') 
  
currentframe = 0

#orignal_video = cv2.VideoWriter('./codethon_vidoes/capture.avi', fourcc, 20.0, (640, 480)) 
#hsv_video = cv2.VideoWriter('./codethon_vidoes/capture_hsv.avi', fourcc, 20.0, (640, 480))

for i in range(1,200):
    _,img=cap.read()
    ret,frame1=cap.read()
    ret,frame2=cap.read()

    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)

    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV) 

    #orignal_video.write(img) 
    #hsv_video.write(hsv)
    
    

    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)<10:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame1,'status: {}'.format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
            if cv2.contourArea(contour) >= 1 and cv2.contourArea(contour) <4:
                lis_1.append(cv2.contourArea(contour))
            elif cv2.contourArea(contour) >=4 and cv2.contourArea(contour) <7:
                lis_2.append(cv2.contourArea(contour))
            elif cv2.contourArea(contour) >=7 and cv2.contourArea(contour) <=10:
                lis_3.append(cv2.contourArea(contour))
            
            col=random.randint(1,9)

            ls.append(cv2.contourArea(contour))
            plt.plot(ls,'o-',color=colors[col-1], label='Motion Intensity')
            plt.grid(axis='y')
            plt.xlabel(' Number Of Motion Detect ')
            plt.ylabel('Density of Motion ')
            plt.legend()
            plt.show()
            
            
            HEADER='&field1={}'.format(cv2.contourArea(contour))
            NEW_URL=URl+KEY+HEADER
            data=urllib.request.urlopen(NEW_URL)
            print(data)

            notifier.show_toast("Alert","Motion is found....",threaded=True,icon_path=None)

            engine.say("Motion is Found ...")
            engine.runAndWait()

            name = './codethon/detection_' + str(currentframe) + '.jpg'
            print ('Saved Image At :- ' + name)
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

    #orignal_video.release()
    #hsv_video.release()
    
    if cv2.waitKey(10)==27:
        break
    
ps.append(len(lis_1))
ps.append(len(lis_2))
ps.append(len(lis_3))

print('No of Count of Low Motion : {}'.format(len(lis_1)))
print('No of Count of Medium Motion : {}'.format(len(lis_2)))
print('No of Count of High Motion : {}'.format(len(lis_3)))

explode = (0.1, 0.1, 0.1) 
labels=['low or None Motion','Medium Motion', 'High Motion']

plt.pie(ps,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True, startangle=90)
plt.legend()

plt.show()

cv2.destroyAllWindows()
cap.release()


