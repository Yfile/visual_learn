# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:33:47 2019

@author: 上上下下左左右右baba
"""
from PIL import Image
from numpy import*
from pylab import*


def imresize(im,sz):
   """ 使用 PIL 对象重新定义图像数组的大小 """
   pil_im = Image.fromarray(uint8(im))
   return array(pil_im.resize(sz))

def histeq(im,nbr_bins=256):   
   """ 对一幅灰度图像进行直方图均衡化 """
   # 计算图像的直方图
   imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
   cdf = imhist.cumsum() # cumulative distribution function
   cdf = 255 * cdf / cdf[-1] # 归一化
   # 使用累积分布函数的线性插值，计算新的像素值
   im2 = interp(im.flatten(),bins[:-1],cdf)
   return (im2.reshape(im.shape), cdf)

im = array(Image.open('phot.jpg').convert('L'))
pil_im = Image.fromarray(uint8(im))
im2,cdf = histeq(im)

imshow(im)
show()
figure()
hist(im.flatten(),128)
show()

imshow(im2)
show()
figure()
hist(im2.flatten(),128)
show()