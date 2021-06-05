import cv2 
import numpy as np
img=cv2.imread("veera2.jpg")
#create image using numpy
'''
img2=np.zeros((225,225,3))
img1=cv2.line(img,(20,6),(20,170),(123,0,200),4)
img1=cv2.line(img,(20,170),(200,170),(123,100,255),4)
img1=cv2.line(img,(200,170),(200,6),(123,50,255),4)
img1=cv2.line(img,(200,6),(20,6),(123,128,255),4)
cv2.imshow("Frame",img1)
'''
#create a rectangle on image
'''
img1=cv2.rectangle(img,(50,7),(170,160),(0,234,78),2)
cv2.imshow("Frame",img1)
'''

#create a circle on image
'''
img1=cv2.circle(img,(110,80),80,(100,234,17),3)
cv2.imshow("Frame",img1)
'''

'''
#create a eclipse on image
img1=cv2.ellipse(img,(60,6),(70,70),0,60,200,255,2)
cv2.imshow("Frame",img1)
'''

'''
#create a polygon on image
pts = np.array([[50,5],[50,170],[170,170],[170,6]], np.int32)
pts = pts.reshape((-1,1,2))
#print(pts)
img1=cv2.polylines(img,[pts],True,(0,234,67),3)
cv2.imshow("Frame",img1)
'''

'''
#put text on image 
img1=cv2.putText(img,"Its me veera",(5,50),cv2.FONT_HERSHEY_COMPLEX,1,(20,255,100),2)
cv2.imshow("Frame",img1)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()
 

























'''    
     |
     |
-----|------
     |
     |
'''