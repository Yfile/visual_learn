#用2版本

from PIL import Image
import os,sys

filelist = os.listdir('D:\work\Python_work\shixun_work\Image')
for infile in filelist:
    outfile = os.path.splitext(infile)[0]+".jpeg"
    print outfile
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print  "cannot convert", infile
