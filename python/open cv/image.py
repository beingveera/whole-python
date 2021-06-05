import cv2 
import numpy as np
img=cv2.imread("veera.jpg")
img1=cv2.imread("veera2.jpg")

#print(img.dtype)
#ball=img[100:200,200:200]
#print(ball)

'''
b,g,r=cv2.split(img)
slr=cv2.merge((b,g,r))
cv2.imshow("Frame",slr)
'''
#border
'''
replicate=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflact=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflact101=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101)
'''

#ADD  to images 
#both images must be same size...
ls=cv2.addWeighted(img,0.5,img1,0.5,0)
cv2.imshow("Frame",ls)


'''
#threshlod binary images...
rows,cols,channels=img1.shape
roi=img[0:rows,0:cols]
bgr=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(bgr,10,255,cv2.THRESH_BINARY)
mask_inv=cv2.bitwise_not(mask)
img_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img_fg=cv2.bitwise_and(img,img1,mask=mask)
ok=cv2.add(img_fg,img_bg)
img1[0:rows,0:cols]=ok
cv2.imshow("Frame",img1)
'''

'''
for i in dir(cv2):
    if i.startswith("COLOR_"):
        print(i)
'''
'''
cv2.imshow("Frame",img1)
'''
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows(0)