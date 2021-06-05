import qrcode 

'''  
# Data to be encoded 
data = 'QR Code using make() fuction'
  
# Encoding data using make() function 
img = qrcode.make(data) 
  
# Saving as an image file 
img.save('MyQRCode1.png')
'''
'''
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('main.png')
'''

'''
import qrcode
from qrcode.image.pure import PymagingImage
img = qrcode.make('Some data here', image_factory=PymagingImage)

img.save('tech.png')
'''

qr = qrcode.QRCode(
	version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
	box_size=5,
	border=5
)
 
# Enter data that you want to store
qr_data = 'Welcome To Simplified Python'
 
# Add data 
qr.add_data(qr_data)
qr.make(fit=True)
 
# Create an image from the QR code instance
img = qr.make_image(fill_color='blue', back_color='white')
 
# Save the image
img.save('qr.png')
 