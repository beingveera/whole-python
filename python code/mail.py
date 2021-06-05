
import nasapy
from datetime import datetime
import urllib.request
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

#Initialize Nasa class by creating an object:
nasa = nasapy.Nasa(key="523p5hPYHGzafYGLCkqa54kKMTV2vbP0XcPxkcLm")

#Get today's date in YYYY-MM-DD format:
d = input("Enter date in YYYY-MM-DD format : ")

#Get the image information:
apod = nasa.picture_of_the_day(date=d, hd=True)

#file name of the image:
title = d+"_"+apod["title"].replace(" ","_").replace(":","_")+".jpg"

#Downloading file only if it's image:
if apod['media_type'] == 'image':
    
        #Downloading the image:
        if 'hdurl' in apod.keys():
            urllib.request.urlretrieve(url = apod["hdurl"] , filename = title)
        else:
            urllib.request.urlretrieve(url = apod["url"] , filename = title)  


        #Sending email:
        
        #Email addresses:
        from_addr = "veerasharma9895@gmail.com"
        to_addr = ["veerasharma0000@gmail.com"]

        #create an instance of MIMEMultipart():
        message = MIMEMultipart() 

        #Subject of the email: 
        message['Subject'] = apod["title"]

        #Body of the email:
        body = "Hello, This is an automatic email by Pratik Shukla.\n\n\n" + apod["explanation"]

        #Attaching the text in body:
        message.attach(MIMEText(body, 'plain')) 

        #Opening the attachment: 
        filename = title

        #Opening file in binary mode:
        attachment = open(filename, "rb") 

        #Creating object of MIMEBase:
        p = MIMEBase('application', 'octet-stream') 

        #Adding header with file name:
        p.add_header('Content-Disposition', 'attachment', filename= title) 

        #Attachment as payload:
        p.set_payload((attachment).read())
        
        #Encoding the payload:
        encoders.encode_base64(p)

        #Attaching the payload with message:
        message.attach(p) 

        #Create smtp server:
        s = smtplib.SMTP('smtp.gmail.com', 587) 

        #Start TLS for security 
        s.starttls() 

        #Credentials authentication 
        s.login(from_addr, password = "9829237552") 

        #Converts the Multipart msg into a string 
        text = message.as_string() 

        #Sending the mail 
        s.sendmail(from_addr, to_addr, text) 

        #Terminating the session 
        s.quit() 

        print("Email sent successfully!")

        
#If media file is not image:
else:
    print("Image not available!")
    print("Email not sent!")
    print("Please enter some other date!!")