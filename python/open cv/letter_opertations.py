import cv2
import numpy as np


img=cv2.imread("veera2.jpg")
ker=np.ones((5,1),np.float32)
print(ker)
img1=cv2.erode(img,ker,iterations=1)
img2=cv2.dilate(img,ker,iterations=1)
img3= cv2.morphologyEx(img, cv2.MORPH_OPEN, ker)
img4 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, ker)
img5= cv2.morphologyEx(img, cv2.MORPH_GRADIENT, ker)
img6= cv2.morphologyEx(img, cv2.MORPH_TOPHAT, ker)
img7 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, ker)



cv2.imshow("frame",img)
cv2.imshow("frame1",img1)
cv2.imshow("frame2",img2)
cv2.imshow("frame3",img3)
cv2.imshow("frame4",img4)
cv2.imshow("frame5",img5)
cv2.imshow("frame6",img6)
cv2.imshow("frame7",img7)
cv2.waitKey(0)




