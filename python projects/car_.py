import cv2
 

img = cv2.imread("car.jpg", cv2.IMREAD_COLOR)
 

cv2.imshow("Cute Kitens", img)
 

cv2.waitKey(0)
 

cv2.destroyAllWindows()