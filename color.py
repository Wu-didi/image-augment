#-*- codeing = utf-8 -*- 
#@Time: 2021/3/28 21:23
#@Author : dapao
#@File : color.py
#@Software: PyCharm



from PIL import Image, ImageDraw
import numpy as np
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb


def rand(a=0, b=1):
    return np.random.rand() * (b - a) + a


def color(line, jitter=.5, hue=.1, sat=1.5, val=1.5,):
    image = Image.open(line)
    # 色域扭曲
    hue = rand(-hue, hue)
    sat = rand(1, sat) if rand() < .5 else 1 / rand(1, sat)
    val = rand(1, val) if rand() < .5 else 1 / rand(1, val)
    x = rgb_to_hsv(np.array(image) / 255.)
    x[..., 0] += hue
    x[..., 0][x[..., 0] > 1] -= 1
    x[..., 0][x[..., 0] < 0] += 1
    x[..., 1] *= sat
    x[..., 2] *= val
    x[x > 1] = 1
    x[x < 0] = 0
    image_data = hsv_to_rgb(x)  # numpy array, 0 to 1

    return image_data





if __name__ == "__main__":
    line = r"D:\python_file2\faster-rcnn-keras/VOCdevkit/VOC2007/JPEGImages/100474-3-20160621054328-Pic.jpg"
    image = color(line)
    img = Image.fromarray((image * 255).astype(np.uint8))  ##实现array到image的转换
    print(img)
    img.show()



