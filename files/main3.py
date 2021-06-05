import cv2 
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture()

ls=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=ls.detectMultiScale(gray,1.2,2)
    cv2.imshow("Frame",gray)
    if ret == True:
        k = cv2.waitKey(60) & 0xff
cv2.destroyAllWindows()
cap.release()

'''
while True:
    ret ,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = ls.detectMultiScale(gray,1.5,5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(200,255,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.imshow("Frame",img)
    if ret == True:
        k = cv2.waitKey(60) & 0xff
cv2.destroyAllWindows()
cap.release()
'''