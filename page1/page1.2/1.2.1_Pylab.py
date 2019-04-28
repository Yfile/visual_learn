from PIL import Image
from pylab import *
# 读取图像到数组中
im = array(Image.open('phot.jpg'))
# 绘制图像
imshow(im)
# 一些点
x = [100,100,400,400]
y = [200,500,200,500]
# 使用红色星状标记绘制点
plot(x,y,'r*')
# 绘制连接前两个点的线
plot(x[:3],y[:3])
# 添加标题，显示绘制的图像
title('Plotting: "phot.jpg"')
axis('off')
show()
