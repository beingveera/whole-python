import cv2 
img=cv2.imread("veera.jpg")
cv2.imwrite("veera.jpg",img)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()