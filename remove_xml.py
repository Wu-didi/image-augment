import numpy as np
import xml.etree.ElementTree as ET
import os
import random
import cv2
import time


xml_path = "206.xml"
tree = ET.parse(xml_path)
root = tree.getroot()
index_list = []
i = 0
for element in root.findall('object'):

    if str(element[0].text) == "with_mask" :
        print(i)
        index_list.append(i)
        root.remove(element)
        #root.remove(root[i])
    i += 1
print(index_list)
#root.remove(root[index_list[0]])
tree.write("206_last_one.xml")  # 保存xml，到指定的地址