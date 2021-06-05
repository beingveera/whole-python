import smtplib as s
from urllib.request import urlopen
import json
import time
import threading



#ketanjainjain27@gmail.com
READ_API_KEY='https://api.thingspeak.com/channels/1223386/feeds.json?results=2'
CHANNEL_ID='1223386'


def data_catch():
    obj=s.SMTP('smtp.gmail.com',587)
    obj.starttls()
    obj.login("smart.iv.user@gmail.com",'9829237552')
    threading.Timer(15,data_catch).start()
    TS = urlopen("https://api.thingspeak.com/channels/{}/feeds.json?api_key={}&results=2".format(CHANNEL_ID,READ_API_KEY))
    response = TS.read()
    data=json.loads(response.decode('utf-8'))

  #  print("Field 1 : {} ".format(data["feeds"][1]["field1"]))
    a=data["feeds"][1]["field2"]
   # print("Field 2 : {} ".format(a))
    subject="Smart IV Team "
    body="\nField 1 : {} \n\n Field 2 : {} ".format(data["feeds"][1]["field1"],a)
    message="Subject:{}\n\n{}".format(subject,body)
    obj.sendmail("smart.iv.user@gmail.com","ketanjainjain27@gmail.com",message)
    print("Send main successfully...")
    obj.quit()




    
if __name__ == '__main__':
    data_catch()
    


