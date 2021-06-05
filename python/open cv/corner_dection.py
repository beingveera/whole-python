import cv2
import numpy as np
filename = 'chess.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.00001)
dst = cv2.dilate(dst,None)
img[dst>0.000001*dst.max()]=[0,0,255]
img_double=cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)
cv2.imshow('dst',img_double)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
