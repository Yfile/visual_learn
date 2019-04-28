# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 09:20:02 2019

@author: 上上下下左左右右baba
"""

#
#from pylab import*
#import matplotlib
#
#from PIL import Image
#
#im = array(Image.open('phot.jpg'))
#imshow(im)
#print ('Please click 3 points')
#x = ginput(3)
#print ('you clicked:',x)
#show()

from PIL import Image
from pylab import *

 
im = array(Image.open('phot.jpg'))
imshow(im)
print('Please click 3 points')
x =ginput(3)
print('you clicked:',x)
show()