import requests 
import shutil 

image_url="https://thingspeak.com/channels/1223386/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15.jpg"

response=requests.get(image_url,stream=True)
file=open("output.png","wb")

response.raw_decode_content=True

shutil.copyfileobj(response.raw,file)
del response