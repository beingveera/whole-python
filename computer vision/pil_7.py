from PIL import * 

img=Image.open(r"C:\\Users\\techno\\Desktop\\calc.png")

r,g,b=img.split()

im=Image.merge('RGB',(b,g,r))

im.show()



