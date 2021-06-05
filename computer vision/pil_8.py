# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 12:53:29 2021

@author: techno
"""

from PIL import * 

img=Image.open(r"C:\\Users\\techno\\Desktop\\calc.png")

im=img.resize((900,700))

out = im.transpose(Image.FLIP_LEFT_RIGHT)
out = im.transpose(Image.FLIP_TOP_BOTTOM)
out = im.transpose(Image.ROTATE_90)
out = im.transpose(Image.ROTATE_180)
out = im.transpose(Image.ROTATE_270)


out.show()