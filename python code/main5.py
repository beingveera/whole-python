import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\techno\\Desktop\\tessarest-ocr\\tesseract.exe"
img = cv2.imread(r"C:\\Users\\techno\\Desktop\\main1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU,cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
im2 = img.copy()
file = open("A.cpp", "w+")
file.write("")
file.close()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cropped = im2[y:y + h, x:x + w]
    file = open("A.cpp", "a")
    text = pytesseract.image_to_string(cropped)
    for m in text:
        file.write(m)
    file.close()
    cv2.resize(im2,(10,10),fx=0.1,fy=0.1,dst=0)
    cv2.imshow('Text Image',im2)
    cv2.waitKey()
    cv2.distoryAllWindows()
