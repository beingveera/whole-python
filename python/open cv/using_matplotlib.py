import numpy as np
import cv2 


img=cv2.imread("veera.jpg")
#pixsel color 
px=img[200,100]
print(px)
cv2.imshow("frame",img)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()