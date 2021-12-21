#-*- codeing = utf-8 -*- 
#@Time: 2021/4/6 15:36
#@Author : dapao
#@File : dealwith_xml.py
#@Software: PyCharm
import cv2
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

path = r"D:\python_file\dataset\make_dateset\TEST_DATASET\Bus\annotations\Bus_10.xml"
save_path  = r'D:\python_file\dataset\make_dateset\TEST_DATASET\Bus'
original_image = cv2.imread(r"D:\python_file\dataset\make_dateset\TEST_DATASET\Bus\images\Bus_10.jpg")
original_y, original_x= original_image.shape[:2]
print(original_x,original_y)
tree = ET.parse(path)
root = tree.getroot()
for xmin_zuobiao in root.iter('xmin'):
    print(xmin_zuobiao.text)
    xmin_zuobiao_ca = xmin_zuobiao.text

for ymin_zuobiao in root.iter('ymin'):
    ymin_zuobiao_ca = ymin_zuobiao.text


for xmax_zuobiao in root.iter('xmax'):
    print(xmax_zuobiao.text)
    xmax_zuobiao_ca = xmax_zuobiao.text

for ymax_zuobiao in root.iter('ymax'):
    ymax_zuobiao_ca = ymax_zuobiao.text

xmin_new = original_x - int(xmax_zuobiao_ca)
xmin_zuobiao.text = str(xmin_new)
xmax_new = original_x - int(xmin_zuobiao_ca)
xmax_zuobiao.text = str(xmax_new)




tree.write(save_path+"1112.xml")  # 保存xml，到指定的地址

print(xmin_zuobiao.text,ymin_zuobiao.text,xmax_zuobiao.text,ymax_zuobiao.text)

image1 = Image.open(r"D:\python_file\dataset\make_dateset\TEST_DATASET\Bus\images\Bus_20.jpg")
draw = ImageDraw.Draw(image1)
draw.rectangle((int(xmin_zuobiao_ca),int(ymin_zuobiao_ca),int(xmax_zuobiao_ca),int(ymax_zuobiao_ca)),fill=None,outline="red",width=5)

image1.show()


image2 = Image.open(r"D:\python_file\dataset\make_dateset\TEST_DATASET\Bus\images\Bus_20.jpg")
image2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
draw = ImageDraw.Draw(image2)
draw.rectangle((int(xmin_zuobiao.text),int(ymin_zuobiao.text),int(xmax_zuobiao.text),int(ymax_zuobiao.text)),fill=None,outline="green",width=5)

image2.show()

