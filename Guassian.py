#-*- codeing = utf-8 -*- 
#@Time: 2021/3/28 20:56
#@Author : dapao
#@File : Guassian.py
#@Software: PyCharm


#对数据集里面的图片添加高斯噪声，主要难点在于同时也要把对应annotations文件
#/xml文件也要对应的保存下来，
#存在问题，图片过大进行高斯噪声处理非常的慢，容易出现问题

import numpy as np
import xml.etree.ElementTree as ET
import os
import random
import cv2
import time

# 高斯模糊：高斯滤波是一种线性平滑低通滤波器，适用于消除高斯噪声，广泛应用于图像处理的减噪过程。
# 滤波高斯就是对整幅图像进行加权平均的过程，每一个像素点的值，都由其本身和邻域内的其他像素值经过加权平均后得到。
# 用一个模板（或称卷积，掩模）扫描图像中的每一个像素，用模板确定的邻域内像素的加权平均灰度值去替代模板中心像素点的值。

def clamp(pv):
    """防止溢出"""
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv


def gaussian_noise_demo(image):
    """添加高斯噪声"""
    h, w, c = image.shape
    for row in range(0, h):
        for col in range(0, w):
            s = np.random.normal(0, 25, 3)  # 产生随机数，每次产生三个
            b = image[row, col, 0]  # blue
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    return image

image = r"D:\python_file2\faster-rcnn-keras/VOCdevkit/VOC2007/JPEGImages/100474-3-20160621054328-Pic.jpg"


image = cv2.imread(image)
gaussian_image = gaussian_noise_demo(image)

        
cv2.imwrite("gaussian.jpg",gaussian_image)
