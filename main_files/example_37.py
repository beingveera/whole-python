import cv2 
import os
import time
from win10toast import ToastNotifier
import pyttsx3
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = 'codingworld.user@gmail.com'
toaddr = "veerasharma0000@gmail.com"

s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(fromaddr, "9829237552") 

msg = MIMEMultipart() 
msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] = "Motion dection Alert "
body = "Motion is found ...\npleace Check....\n\nAlert from Motion Dection...."
msg.attach(MIMEText(body, 'plain')) 


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

notifier=ToastNotifier()
cap=cv2.VideoCapture(0)
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
currentframe = 0

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
            if ret1: 
                name = './data/frame' + str(currentframe) + '.jpg'
                print ('Creating...' + name) 
                cv2.imwrite(name, frame1)
                currentframe += 1

                filename = 'frame' + str(currentframe-1) + '.jpg' 
                attachment = open("C:\\Users\\techno\\data\\frame" + str(currentframe-1) + '.jpg', "rb")
                p = MIMEBase('application', 'octet-stream') 
                p.set_payload((attachment).read()) 
                encoders.encode_base64(p) 
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(p) 

                text = msg.as_string()
                s.sendmail(fromaddr, toaddr, text)


                notifier.show_toast("Alert","Motion is found....",threaded=True,icon_path=None,duration=5)
                engine.say("Motion is Found ...")
                engine.runAndWait()
                while notifier.notification_active():
                    time.sleep(0.1)
                    

            else: 
                break
            continue

        (x,y,w,h)=cv2.boundingRect(i)
        cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,0,255),2)
    
    cv2.imshow("Rectangle",frame2)

    if cv2.waitKey(20) == ord('q'):
        break
cap.release()
cv2.distoryAllWindows()


 
