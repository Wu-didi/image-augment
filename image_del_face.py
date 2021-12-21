#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import xml.dom.minidom
import cv2 as cv
import numpy as np
import cv2
from tqdm import tqdm
with_mask = 0
without_mask = 0
other_mask = 0
ImgPath = 'C:/Users/liangzai/Desktop/other_mask'
AnnoPath = 'C:/Users/liangzai/Desktop/train_annotations'
FinalPath ='C:/Users/liangzai/Desktop/other_mask_out1'
imagelist = os.listdir(ImgPath)

for image in tqdm(imagelist):
    image_pre, ext = os.path.splitext(image)
    a = image[-8 : -4]
    print(a)
    path = r"C:/Users/liangzai/Desktop/other_mask/%s.png" % a
    imgfile = ImgPath +"/"+ image
    xmlfile = AnnoPath +"/"+ image_pre + '.xml'
    finalfile = FinalPath +"/"+ a + '(1)' + '.png'
    per_image_Rmean = []
    per_image_Gmean = []
    per_image_Bmean = []

    img = cv2.imread(path)
    per_image_Bmean.append(np.mean(img[:,:,0]))
    per_image_Gmean.append(np.mean(img[:,:,1]))
    per_image_Rmean.append(np.mean(img[:,:,2]))
    B = np.mean(per_image_Rmean)
    G = np.mean(per_image_Gmean)
    R = np.mean(per_image_Bmean)

    # 打开xml文档
    DOMTree = xml.dom.minidom.parse(xmlfile)
    # 得到文档元素对象
    collection = DOMTree.documentElement
    # 读取图片
    img = cv.imread(imgfile)

    filenamelist = collection.getElementsByTagName("filename")
    filename = filenamelist[0].childNodes[0].data
    # print(filename)
    # 得到标签名为object的信息
    objectlist = collection.getElementsByTagName("object")
    

    for objects in objectlist:
        # 每个object中得到子标签名为name的信息
        namelist = objects.getElementsByTagName('name')
        # 通过此语句得到具体的某个name的值
        objectname = namelist[0].childNodes[0].data

        bndbox = objects.getElementsByTagName('bndbox')
        
        if not (objectname == 'mask_weared_incorrect') :
            for box in bndbox:       
                x1_list = box.getElementsByTagName('xmin')
                x1 = int(float(x1_list[0].childNodes[0].data))
                y1_list = box.getElementsByTagName('ymin')
                y1 = int(float(y1_list[0].childNodes[0].data))
                x2_list = box.getElementsByTagName('xmax')
                x2 = int(float(x2_list[0].childNodes[0].data))
                y2_list = box.getElementsByTagName('ymax')
                y2 = int(float(y2_list[0].childNodes[0].data))
                cv.rectangle(img, (x1, y1), (x2, y2), (R, G, B), thickness= -1)
                
                cv.imwrite('%s' % finalfile, img)

