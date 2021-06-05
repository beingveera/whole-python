import cv2 
import numpy as np
'''
img=cv2.imread("veera.jpg")
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("Frame1",thresh1)
cv2.imshow("Frame2",thresh2)
cv2.imshow("Frame3",thresh3)
cv2.imshow("Frame4",thresh4)
cv2.imshow("Frame5",thresh5)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
'''

img=cv2.imread("suduko.jpg",0)
img1=cv2.medianBlur(img,3)
ret,th1=cv2.threshold(img1,110,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th4=cv2.adaptiveThreshold(th1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th5=cv2.adaptiveThreshold(th1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("Frame1",th1)
cv2.imshow("Frame2",th2)
cv2.imshow("Frame3",th3)
cv2.imshow("Frame4",th4)
cv2.imshow("Frame5",th5)
k=cv2.waitKey(0)
if k ==27:
    cv2.destroyAllWindows()
