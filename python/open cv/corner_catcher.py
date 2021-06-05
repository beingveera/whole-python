import numpy as np
from cv2 import cv2
cap = cv2.VideoCapture(0)
while True:
    ret ,img = cap.read()
    cv2.imshow("real",img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.0001)
    dst = cv2.dilate(dst,None)
    img[dst>0.00001*dst.max()]=[0,0,255]
    cv2.imshow('dst',img)
    if ret == True:
        k = cv2.waitKey(60) & 0xff
cv2.destroyAllWindows()
cap.release()
