from PIL import * 

img=Image.open(r"C:\\Users\\techno\\Desktop\\calc.png")

crp=(200,200,900,900)
im=img.crop(crp)

im.paste(im,crp)

im.show()


