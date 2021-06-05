import numpy as np
import cv2 

'''
#Scalling of images
img=cv2.imread("veera2.jpg")
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
height,width=img.shape[:2]
resp=cv2.resize(img,(2*height,2*width),interpolation=cv2.INTER_CUBIC)
cv2.imshow("Frame",resp)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
'''
'''
img=cv2.imread("veera2.jpg",0)
rows,cols=img.shape
m=np.float32([[30,10,10],[0,10,30]])
dst=cv2.warpAffine(img,m,(cols,rows))
cv2.imshow("Frame",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
img = cv2.imread('veera.jpg',0)
rows,cols = img.shape
M = cv2.getRotationMatrix2D((cols/3,rows/2),54,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("Frame",dst)
cv2.waitKey(0)
cv2.destoryAllWindows()
'''

'''
img = cv2.imread('veera1.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("Frame",dst)
cv2.waitKey(0)
cv2.destoryAllWindows()
'''
'''
img = cv2.imread('suduko.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
cv2.imshow("Frame",dst)
cv2.waitKey(0)
cv2.destoryAllWindows()
'''


