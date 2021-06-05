import cv2 
import numpy as np
'''
for i in dir(cv2):
    if "EVENT_" in i:
        print(i)
EVENT_FLAG_ALTKEY
EVENT_FLAG_CTRLKEY
EVENT_FLAG_LBUTTON
EVENT_FLAG_MBUTTON
EVENT_FLAG_RBUTTON
EVENT_FLAG_SHIFTKEY
EVENT_LBUTTONDBLCLK #2 times on keypad
EVENT_LBUTTONDOWN
EVENT_LBUTTONUP
EVENT_MBUTTONDBLCLK
EVENT_MBUTTONDOWN
EVENT_MBUTTONUP
EVENT_MOUSEHWHEEL
EVENT_MOUSEMOVE
EVENT_MOUSEWHEEL
EVENT_RBUTTONDBLCLK
EVENT_RBUTTONDOWN
EVENT_RBUTTONUP
    '''
'''
img=cv2.imread("veera.jpg")
#img = np.zeros((512,512,3), np.uint8)

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),70,(255,100,255),2)
cv2.namedWindow("veera")
cv2.setMouseCallback('veera',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()       
'''
'''
img=cv2.imread("veera1.jpg")
def draw_line(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.line(img,(x,y),(x+20,y+20),(0,234,200),2)

cv2.namedWindow("techno")
cv2.setMouseCallback("techno",draw_line)
while(1):
    cv2.imshow("image",img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()  
'''

'''
def nothing(x):
    pass
img=np.zeros((300,300,3),np.uint8)
cv2.namedWindow("Color")
cv2.createTrackbar("R","Color",0,255,nothing)
cv2.createTrackbar("G","Color",0,255,nothing)
cv2.createTrackbar("B","Color",0,255,nothing)
switch='0 : OFF \n1 : ON'
cv2.createTrackbar(switch,"Color",0,1,nothing)

while(True):
    cv2.imshow("frame",img)
    k=cv2.waitKey(1) and 0xFF
    if k== 27:
        break

    r=cv2.getTrackbarPos("R","Color",)
    g=cv2.getTrackbarPos("G","Color")
    b=cv2.getTrackbarPos("B","Color")
    s=cv2.getTrackbarPos(switch,"Color")

    if s == 0:
        img[:] = 0
    else:
        img[:]=[b,g,r]
    
cv2.destroyAllWindows()
'''