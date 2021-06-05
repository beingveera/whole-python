from urllib.request import urlopen

import json
import time


READ_API_KEY='https://api.thingspeak.com/channels/1223386/feeds.json?results=2'
CHANNEL_ID='1223386'


while True:
    TS = urlopen("https://api.thingspeak.com/channels/{}/feeds.json?api_key={}&results=2".format(CHANNEL_ID,READ_API_KEY))
    response = TS.read()
    data=json.loads(response.decode('utf-8'))
   # print(data)
    print("Field 1 : {} ".format(data["feeds"][1]["field1"]))
    a=data["feeds"][1]["field2"]
    print("Field 2 : {} ".format(a))
    TS.close()
