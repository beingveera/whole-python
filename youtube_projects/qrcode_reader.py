import pyqrcode 
from pyzbar.pyzbar import decode 
from PIL import Image 


qr=pyqrcode.create('Its me veera')
qr.png('myqrcode.png',scale=8)



d=decode(Image.open('myqrcode.png'))
print(d)