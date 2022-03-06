# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:51:07 2022

@author: olavg
"""

import requests
from bs4 import BeautifulSoup as bs
from fpdf import FPDF
from PIL import Image
from io import BytesIO
from math import ceil

#setup image
test_link = 'https://cdn.onepiecechapters.com/file/CDN-M-A-N/op_1040_fallingondeafears_014.png'
img_to_save = requests.get(test_link).content
img_name = test_link.split("/")[-1]

# save original
with open(img_name[:-4] + '_original.png', 'wb') as handler:
    handler.write(img_to_save)

img_obj = Image.open(BytesIO(img_to_save)) #make PIL image from file object from bytes
img_obj_gray = img_obj.convert('L')
img_obj_gray.save(img_name[:-4] + '_grayscale.png')

width, height = img_obj_gray.size
if width > height*1.20:
    left_page = img_obj_gray.crop((0,0,ceil(width/2),height))
    right_page = img_obj_gray.crop((ceil(width/2),0,width,height))
    left_page.save(img_name[:-4] + '_left.png')
    right_page.save(img_name[:-4] + '_right.png')