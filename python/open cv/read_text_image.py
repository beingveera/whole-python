from PIL import Image , ImageTk
from PIL import ImageFilter

file=r"C:\Users\techno\Desktop\open cv\flower1.jpg"
img=Image.open(file)
img.crop(box=(400,500,500,300))
img.show()

img2=img.filter(ImageFilter.EMBOSS)
img2.show()
