# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:32:42 2021

@author: techno
"""

from PIL import *
pil_img=Image.open(r"C:\Users\techno\Whole python\computer vision\one.jpg")
pil_img.convert('L')
pil_img.show()
