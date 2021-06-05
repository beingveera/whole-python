'''
from tkinter import * 
from tkinter import messagebox

def stop():
    cv2.destroyAllWindows()
    cap.release()

def Start():
    import numpy as np
    from cv2 import cv2
    import os
    cap = cv2.VideoCapture('test.mp4')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    if not os.path.exists('data'):
        os.makedirs('data')
    current_frame=0
    while True:   
        ret ,img = cap.read()
        if ret:
            name='./data/frame' + str(current_frame)+'.jpg'
            cv2.imwrite(name,img)
            current_frame += 1
            if current_frame >=10:
                pass
        else:
            break

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,10)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(200,255,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_color)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            if img != "\0":
                print(img)
                cv2.imshow("Frame",img)
            if ret == True:
                k = cv2.waitKey(60) & 0xff
    cv2.destroyAllWindows()
    cap.release()
 
root=Tk()
root.geometry("200x200")

butt1=Button(root,text="Start",bg="yellow",fg="red",border=4,width=5,command=Start).place(x=20,y=50)
butt2=Button(root,text="Stop",bg="yellow",fg="red",border=4,width=5,command=quit).place(x=100,y=50)

root.mainloop()
'''

import numpy as np
from cv2 import cv2
cap = cv2.VideoCapture('test.mp4')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")
body_cascade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
while True:
    ret ,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,3)
    body = body_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(200,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_color)
        smile = smile_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        if img != "\0":
            print(img)
            cv2.imshow("Frame",img)
    if ret == True:
        k = cv2.waitKey(60) & 0xff
cv2.destroyAllWindows()
cap.release()

