# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:17:45 2019

@author: 上上下下左左右右baba
"""

from PIL import Image
import numpy

im = array(Image.open('phot.jpg'))
print (im.shape, im.dtype)
im = array(Image.open('phot.jpg').convert('L'),'f')
print (im.shape, im.dtype)