# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:34:49 2019

@author: 上上下下左左右右baba
"""
from numpy import*
from PIL import Image

im = array(Image.open('phot.jpg').convert('L'))
im2 = 255-im #对图像进行反相处理
im3 = (100.0/255) * im + 100 #将图像像素值变换到100...200区间
im4 = 255.0 * (im/255.0)**2 # 对图像像素值求平方后得到的图像

print(int(im.min()),int(im.max()))
print(int(im2.min()),int(im2.max()))
print(int(im3.min()),int(im3.max()))
print(int(im4.min()),int(im4.max()))

img2 = Image.fromarray(im2.astype('uint8'))
img3 = Image.fromarray(im3.astype('uint8'))
img4 = Image.fromarray(im4.astype('uint8'))  

img2.show()
img3.show()
img4.show()
