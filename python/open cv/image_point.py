import cv2 
import numpy as np 

'''
img=cv2.imread("suduko.jpg",0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow("Image",img)
cv2.imshow("Laplacian",laplacian)
cv2.imshow("SobelX",sobelx)
cv2.imshow("SobelY",sobely)
cv2.waitKey(0)
'''
'''
img=cv2.imread("suduko.jpg",0)
edges = cv2.Canny(img,150,200)
cv2.imshow("Image",edges)
cv2.imshow("Frame",img)
cv2.waitKey(0)
'''

import cv2
import numpy as np

img_rgb = cv2.imread('veera2.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('test.jpg',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imwrite('techno.jpg',img_rgb)

cv2.imshow("frame",img_rgb)
cv2.waitKey(0)





