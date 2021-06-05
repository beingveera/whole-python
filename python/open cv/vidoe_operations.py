import numpy as nps
import cv2 

#save the vidoe
cap=cv2.VideoCapture(0)
fore=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("lokesh.avi",fore,20.0,(640,480))
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        #rotate the window
        frame=cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow("Vidoe",frame)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
