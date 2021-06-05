import cv2 
import numpy as np

'''
#start vidoe camera
cap=cv2.VideoCapture(0)
while(True):
    _, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
cap.release() 
cv2.destroyAllWindows()
'''

cap=cv2.VideoCapture(0)
while(True):
    _, frame = cap.read()
    # hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2XYZ)
    #hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2YUV)
    #hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)
    #hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower=np.array([100,50,50])
    upper=np.array([130,255,255])
    #mask image
    mask=cv2.inRange(hsv,lower,upper)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("res",res)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
cap.release() 
cv2.destroyAllWindows()
