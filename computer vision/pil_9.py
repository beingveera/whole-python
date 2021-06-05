# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:04:46 2021

@author: techno
"""

from PIL import ImageFilter

img=Image.open(r"C:\\Users\\techno\\Desktop\\calc.png")
out = img.filter(ImageFilter.DETAIL)
print(out)
out = im.point(lambda i: i * 1.9)
out.show()