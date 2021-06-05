import cv2 
img=cv2.imread("veera.jpg")
#print(img.item(10,10,2))
img.itemset((10,10,2),255)
print(img.item(10,10,2))
cv2.imshow("frame",img)
k=cv2.waitKey(0)
if k ==27:
    cv2.destroyAllWindows()