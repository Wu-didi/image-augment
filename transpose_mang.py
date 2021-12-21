#-*- codeing = utf-8 -*- 
#@Time: 2021/4/6 16:06
#@Author : dapao
#@File : transpose_mang.py
#@Software: PyCharm

from PIL import Image, ImageDraw
#对数据集里面的图片添加高斯噪声，主要难点在于同时也要把对应annotations文件
#/xml文件也要对应的保存下来，
#存在问题，图片过大进行高斯噪声处理非常的慢，容易出现问题

import numpy as np
import xml.etree.ElementTree as ET
import os
import random
import cv2
import time


#classes = ['Bus', 'Microbus', 'Minivan', 'SUV', 'Truck']

num = 302
classes = ['Bus']
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
    print(original_image_path_list)
    print(len(original_image_path_list))


    #对产生的列表进行shuffle打乱，后面在进行某项变换的时候，有些图片不需要进行变换，随机抽取
    random.shuffle(original_image_path_list)
    print(original_image_path_list)
    print(len(original_image_path_list))
    #利用上面返回的列表去循环每一个图片，并对每一张图片进行高斯噪声

    for single_image_name in original_image_path_list[:num]:
        print(single_image_name,"\n")
        #具体到每一个图片的路径
        original_single_image_path = original_image_path+"\\"+ single_image_name
        print(original_single_image_path)

        image_name = single_image_name.split(".")[0]
        print(image_name)#去掉每个个图片的格式信息，只保留图片名，去掉”.jpg“

        original_image = cv2.imread(original_single_image_path)
        original_y, original_x = original_image.shape[:2]


        # 利用PIL库打开图片，进行变换
        image = Image.open(original_single_image_path)
        image = image.transpose(Image.FLIP_LEFT_RIGHT)

        image.save(image_save_path+"\\"+image_name+"_T"+".jpg")


        #-------------保存xml文件,需要对xml文件里面的坐标进行翻转变换-----------------------------------------
        #打开与与图片名字对应的xml文件
        original_single_xml_path = original_xml_path+"\\"+image_name+".xml"
        print(original_single_xml_path)
        tree = ET.parse(original_single_xml_path)
        root = tree.getroot()

        for xmin_zuobiao in root.iter('xmin'):
            print(xmin_zuobiao.text)
            xmin_zuobiao_ca = xmin_zuobiao.text

        for xmax_zuobiao in root.iter('xmax'):
            print(xmax_zuobiao.text)
            xmax_zuobiao_ca = xmax_zuobiao.text

        xmin_new = original_x - int(xmax_zuobiao_ca)
        xmin_zuobiao.text = str(xmin_new)
        xmax_new = original_x - int(xmin_zuobiao_ca)
        xmax_zuobiao.text = str(xmax_new)

        tree.write(xml_save_path+"\\"+image_name+"_T"+".xml")  # 保存xml，到指定的地址
        print("已经完成处理:", original_image_path_list.index(single_image_name) + 1, "/", len(original_image_path_list))
