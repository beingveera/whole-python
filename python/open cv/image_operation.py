import cv2 
import numpy as np

img=cv2.imread("Veera.jpg")

'''
#smoothing og image
kr=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-2,kr)
cv2.imshow("Frame1",img)
cv2.imshow("Frame",dst)
cv2.waitKey(0)
'''
'''
#blur the iamge
img1=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("frame",img)
cv2.imshow("frame1",img1)
cv2.waitKey(0)
'''
'''
#median felting
img1=cv2.medianBlur(img,7)
cv2.imshow("frame",img)
cv2.imshow("frame1",img1)
cv2.waitKey(0)
'''
'''
#bilaterafilter
img1=cv2.bilateralFilter(img,10,50,50)
cv2.imshow("frame",img)
cv2.imshow("frame1",img1)
cv2.waitKey(0)
'''

