from PIL import * 

img=Image.open(r"C:\\Users\\techno\\Desktop\\calc.png")

crp=(0,0,600,600)
im=img.crop(crp)

im=im.transpose(Image.ROTATE_180)

im.show()


