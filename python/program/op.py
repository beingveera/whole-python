import urllib.request
import requests
import threading
import json

import random

def thingspeak_post():
    threading.Timer(2,thingspeak_post).start()
    val=random.randint(1,100)
    URl='https://api.thingspeak.com/update?api_key=IVPU7JIGDI8ABWP2&field1=0'
    KEY= 'IVPU7JIGDI8ABWP2'
    HEADER='&field1={}&field2={}&field3'.format(val,val)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)
    
if __name__ == '__main__':
    thingspeak_post()