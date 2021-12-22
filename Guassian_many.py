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
            s = np.random.normal(0, 3, 3)  # 产生随机数，每次产生三个
            b = image[row, col, 0]  # blue
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    return image
#classes = ['Bus', 'Microbus', 'Minivan', 'SUV', 'Truck']
num = 215
classes = ['Truck']
images_annotatins = ['images','annotations']
original_path = r"D:\python_file\dataset\make_dateset\backups\datasetv3.0"
save_path = r"D:\python_file\dataset\make_dateset\backups\data"
for car in classes:
    print("开始处理车型:",car)
    original_image_path = original_path+"\\"+car+"\\"+images_annotatins[0]
    original_xml_path = original_path+"\\"+car+"\\"+images_annotatins[1]
    image_save_path = save_path+"\\"+car+"\\"+images_annotatins[0]
    xml_save_path = save_path+"\\"+car+"\\"+images_annotatins[1]


    original_image_path_list = os.listdir(original_image_path)
    #返回的值是一个以文件名组成的列表
    print("车型数量为：",len(original_image_path_list))


    #对产生的列表进行shuffle打乱，后面在进行某项变换的时候，有些图片不需要进行变换，随机抽取
    random.shuffle(original_image_path_list)
    print(original_image_path_list)
    # print(len(original_image_path_list))
    #利用上面返回的列表去循环每一个图片，并对每一张图片进行高斯噪声

    for single_image_name in original_image_path_list[:num]:
        start = time.time()
        #print(single_image_name,"\n")
        #print("开始处理",original_image_path_list.index(single_image_name)+1,"/",len(original_image_path_list))
        #具体到每一个图片的路径
        original_single_image_path = original_image_path+"\\"+ single_image_name
        #print(original_single_image_path)
        #利用cv2打开图片，进行变换
        original_image_cv2 = cv2.imread(original_single_image_path)

        # 图片过大，适当缩小一些，便于出来操作
        x, y = 0.3, 0.3
        original_y, original_x = original_image_cv2.shape[:2]
        resize_image = cv2.resize(original_image_cv2,
                                  (int(original_x * x),
                                   int(original_y * y)),
                                  interpolation=cv2.INTER_CUBIC)
        # cv2.imshow("resize_image",resize_image)


        # print(original_image_cv2.shape)

        gaussian_image = gaussian_noise_demo(resize_image)

        x, y = 1, 1
        #original_y, original_x = original_image_cv2.shape[:2]
        gaussian_image = cv2.resize(gaussian_image,
                                  (int(original_x * x),
                                   int(original_y * y)),
                                  interpolation=cv2.INTER_CUBIC)


        image_name = single_image_name.split(".")[0]#将图片的文件名单独取出来
        # print(image_name)
        cv2.imwrite(image_save_path+"\\"+image_name+"_G"+".jpg",gaussian_image)
        #保存xml文件
        #打开与与图片名字对应的xml文件
        original_single_xml_path = original_xml_path+"\\"+image_name+".xml"
        # print(original_single_xml_path)
        tree = ET.parse(original_single_xml_path)
        root = tree.getroot()
        # print(original_xml_path+"\\"+image_name+"_G"+".xml")
        tree.write(xml_save_path+"\\"+image_name+"_G"+".xml")#保存新的XML文件
        end = time.time()
        print("已经完成处理:",original_image_path_list.index(single_image_name)+1,"/",len(original_image_path_list),"花费时间为:",start-end)
