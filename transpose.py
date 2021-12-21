#-*- codeing = utf-8 -*- 
#@Time: 2021/3/28 21:17
#@Author : dapao
#@File : transpose.py
#@Software: PyCharm

from PIL import Image, ImageDraw
import numpy as np
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb


line = r"D:\python_file2\faster-rcnn-keras/VOCdevkit/VOC2007/JPEGImages/100474-3-20160621054328-Pic.jpg"

if True:

    image = Image.open(line)
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    image.save("transpose.jpg")
    image.show()