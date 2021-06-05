import urllib.request
import urllib
import json
import re
#write data on thinks peak
#ls= urllib.request.urlopen('https://api.thingspeak.com/update?api_key=IVPU7JIGDI8ABWP2&field1='+str(100))
#print(ls)


#read data from thinks peak
'''
ls=urllib.request.urlopen("https://thingspeak.com/channels/1223386/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15")
ps=ls.read()
print(ps)
'''
ls=urllib.request.urlretrieve("https://thingspeak.com/channels/1223386/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15.jpg")
print(ls)