import cv2
import pytesseract 
pytesseract.pytesseract.tesseract_cmd=r"C:\\Users\\techno\\Desktop\\tessarest-ocr\\tesseract.exe"
img=cv2.imread("C:\\Users\\techno\\Desktop\\python\\open cv\\smart_iv_soft.png")
text=pytesseract.image_to_string(img)
print(text)
