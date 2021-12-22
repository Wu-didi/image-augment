#-*- codeing = utf-8 -*- 
#@Time: 2021/4/7 19:08
#@Author : dapao
#@File : color_mang.py
#@Software: PyCharm

import xml.etree.ElementTree as ET
import os
import random
from PIL import Image
import time
import numpy as np
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb


def rand(a=0, b=1):
    return np.random.rand() * (b - a) + a


def color(path, jitter=.5, hue=.1, sat=1.5, val=1.5,):
    image = Image.open(path)
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
    img = Image.fromarray((image_data * 255).astype(np.uint8))  ##实现array到image的转换
    return img

#classes = ['Bus', 'Microbus', 'Minivan', 'SUV', 'Truck']
num = 125  #需要进行增广的数量
classes = ['SUV']
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

        image_name = single_image_name.split(".")[0]
        print(image_name)  # 去掉每个个图片的格式信息，只保留图片名，去掉”.jpg“

        image = color(original_single_image_path)
        image.save(image_save_path + "\\" + image_name + "_C" + ".jpg")
        image_name = single_image_name.split(".")[0]#将图片的文件名单独取出来

        #保存xml文件
        #打开与与图片名字对应的xml文件
        original_single_xml_path = original_xml_path+"\\"+image_name+".xml"
        # print(original_single_xml_path)
        tree = ET.parse(original_single_xml_path)
        root = tree.getroot()
        # print(original_xml_path+"\\"+image_name+"_G"+".xml")
        tree.write(xml_save_path+"\\"+image_name+"_C"+".xml")#保存新的XML文件
        end = time.time()
        print("已经完成处理:",original_image_path_list.index(single_image_name)+1,"/",len(original_image_path_list),"----花费时间为:",start-end)



