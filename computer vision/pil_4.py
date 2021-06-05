from PIL import * 

img=Image.open(r"C:\\Users\\techno\\Desktop\\calc.png")

crp=(100,100,400,400)
im=img.crop(crp)
im.show()


