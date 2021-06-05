import cv2 

cap=cv2.VideoCapture("C:\\Users\\techno\\Desktop\\yenti\\love.mp4")

while True:
    ret1,frame1=cap.read()
    gary1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    gray1=cv2.GaussianBlur(gary1,(21,21),0)
    cv2.imshow("Real",frame1)

    ret2,frame2=cap.read()
    gary2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    gray2=cv2.GaussianBlur(gary2,(21,21),0)

    deltaframe=cv2.absdiff(gray1,gray2)
    cv2.imshow("delta",deltaframe)

    threshold=cv2.threshold(deltaframe,25,255,cv2.THRESH_BINARY)[1]
    threshold=cv2.dilate(threshold,None)
    cv2.imshow("threshold",threshold)

    contor,heirechy=cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for i in contor:
        if cv2.contourArea(i)<30:
            continue

        (x,y,w,h)=cv2.boundingRect(i)
        cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("Rectangle",frame2)

    if cv2.waitKey(20) == ord('q'):
        break
cap.release()
cv2.distoryAllWindows()
