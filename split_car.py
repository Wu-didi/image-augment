
#-*- codeing = utf-8 -*-
#@Time: 2021/4/18 9:26
#@Author : dapao
#@File : split_car.py
#@Software: PyCharm


#将训练集中的车辆按照车型进行分类，然后进行一定的扩充
import cv2
import os
import xml.etree.ElementTree as ET

oringinal_xml_path = r"D:\python_file2\faster-rcnn-keras\VOCdevkit\VOC2007\Annotations"
oringinal_image_path = r"D:\python_file2\faster-rcnn-keras\VOCdevkit\VOC2007\JPEGImages"
image_ids = open(r'D:\python_file2\faster-rcnn-keras\VOCdevkit\VOC2007\ImageSets\Main\train.txt').read().strip().split()
print(image_ids)

number_Sedan = 0
number_SUV = 0
number_Bus = 0
number_Truck = 0
number_Minivan = 0
number_Microbus = 0


classes = ['Bus', 'Microbus', 'Minivan', 'Sedan', 'SUV', 'Truck']

#这个函数用来读取图片，然后保存到指定的位置
def save_carimage_class(image_path,car_class,index):
    save_image_path = 'D:\\python_file\\dataset\\make_dateset\\datasetv4.0' + '\\' + car_class +'\\'+ 'images' #图片的保存路径
    if not os.path.exists(save_image_path):#如果不存在该文件夹，下面就会创建一个
        os.mkdir(save_image_path)
    img = cv2.imread(image_path)#读取图片
    cv2.imwrite(save_image_path +'\\' + car_class+"_"+str(index)+ '.jpg', img)#保存图片，到指定的地址

#定义一个函数用来保存xml文件
def save_xml(xml_info,car_class,index):
    save_image_path = 'D:\\python_file\\dataset\\make_dateset\\datasetv4.0' + '\\' + car_class+'\\'+ 'annotations'#xml标签各类车辆的保存路径
    if not os.path.exists(save_image_path):#如果不存在该文件夹，下面就会创建一个
        os.mkdir(save_image_path)
    xml_info.write(save_image_path + '\\' + car_class+"_"+str(index)+ '.xml')#保存xml，到指定的地址


for image_name in image_ids:
    index = image_ids.index(image_name)
    print(image_name)
    every_image_path = oringinal_image_path+"\\"+image_name+".jpg"
    every_xml_path = oringinal_xml_path+"\\"+image_name+".xml"
    print(every_xml_path)
    print(every_image_path)
    tree = ET.parse(every_xml_path)
    root = tree.getroot()
    for obj in root.iter('object'):
        difficult = 0
        if obj.find('difficult') != None:
            difficult = obj.find('difficult').text
        car_class = obj.find('name').text
    print(car_class)

    if car_class == 'Sedan':
        number_Sedan+=1
        save_carimage_class(every_image_path, car_class, index)
        save_xml(tree,car_class,index)
    elif car_class =='SUV':
        number_SUV += 1
        save_carimage_class(every_image_path, car_class, index)
        save_xml(tree,car_class,index)
    elif car_class == 'Minivan':
        number_Minivan += 1
        save_carimage_class(every_image_path, car_class, index)
        save_xml(tree,car_class,index)
    elif car_class == 'Truck':
        number_Truck += 1
        save_carimage_class(every_image_path, car_class, index)
        save_xml(tree,car_class,index)
    elif car_class == 'Microbus':
        number_Microbus += 1
        save_carimage_class(every_image_path, car_class, index)
        save_xml(tree,car_class,index)
    else:
        number_Bus +=1
        save_carimage_class(every_image_path, car_class, index)
        save_xml(tree,car_class,index)

print(number_Bus,number_Microbus,number_Truck,number_Minivan,number_SUV,number_Sedan)
