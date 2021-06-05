import cv2
import numpy as np
import pyautogui
import imutils



cap = cv2.VideoCapture(0);

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = imutils.resize(frame,height=700, width=900)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowred = np.array([131,90,106])
    highred = np.array([255,255,255])

    lowblue = np.array([40,150,116])
    highblue = np.array([255,255,255])

    red_mask = cv2.inRange(hsv, lowred, highred)
    blue_mask = cv2.inRange(hsv, lowblue, highblue)

   
    #for the red Object
    contours,hierachy=cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    #startpoint, endpoint, color, thicknessqeeeeeeeeeee
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,0,255),2)  
         
         
        
        
        
    
    #for the blue Object
    contours,hierachy=cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x + w, y + h),(255,0,0),2)

    
    
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()