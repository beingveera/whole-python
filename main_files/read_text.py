from cv2 import cv2 
import pytesseract

img=cv2.imread("veera.jpg")
text=pytesseract.image_to_string(img)
print(text)