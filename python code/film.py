import cv2
import os
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\\Users\\techno\\Desktop\\tessarest-ocr\\tesseract.exe"
cam = cv2.VideoCapture(r"C:\\Users\\techno\\Desktop\\yenti\\js.mp4")
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')
currentframe = 0
while(True):
    ret,frame = cam.read()
    if ret:
        name = './data/frame' + str(currentframe) + '.png'
        #print ('Creating...' + name)
        cv2.imwrite(name, frame)
        img=cv2.imread(r"C:\\Users\\techno\\data\\frame{}.png".format(currentframe))
        text=pytesseract.image_to_string(img)
        with open('techno.txt','a') as kl:
            kl.write(text)
            kl.write("\n")
        print(text)
        currentframe += 1
       # time.sleep(.5)
    else:
        break
cam.release()
cv2.destroyAllWindows() 



 



