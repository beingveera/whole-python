
import numpy as np
from cv2 import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
smile_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")
body_cascade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
while True:
    ret ,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.5,2)
    
    

    #faces=face_cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.2,3)
        smile = smile_cascade.detectMultiScale(roi_gray,1.1,1)
        body=body_cascade.detectMultiScale(roi_gray,1.1,2)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        if img != "\0":
            print(img)
            cv2.imshow("Frame",img)
    if ret == True:
        k = cv2.waitKey(60) & 0xff
cv2.destroyAllWindows()
cap.release()

