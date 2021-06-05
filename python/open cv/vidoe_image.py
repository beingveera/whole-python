import cv2 
import numpy as np


cap=cv2.VideoCapture(0)
img=cv2.imread('tech.png')
#cap=cv2.imread('opencv.mp4',flags=2)

orb=cv2.ORB_create(nfeatures=1000)
kp1,des1=orb.detectAndCompute(img,None)

while True:
    suss,img_web=cap.read()
    kp2,des2=orb.detectAndCompute(img_web,None)
    img_web=cv2.drawKeypoints(img_web,kp2,None)

    bf=cv2.BFMatcher()
    matchs=bf.knnMatch(des1,des2,k=2)
    good=[]

    for m,n in matchs:
        if m.distance <0.75*n.distance:
            good.append(m)
    print(len(good))
    img_feature=cv2.drawMatches(img,kp1,img_web,kp2,good,None,flags=2)




    ht,wt,ct = img.shape
    img_web=cv2.resize(img_web,(wt,ht))
    cv2.imshow('img',img)
    cv2.imshow('vid',img_web)
    cv2.imshow('img_feature',img_feature)



    if cv2.waitKey(20) == ord('q'):
        break
cap.release()
cv2.distoryAllWindows()
