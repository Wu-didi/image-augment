#-*- codeing = utf-8 -*- 
#@Time: 2021/4/7 10:43
#@Author : dapao
#@File : test.py
#@Software: PyCharm
# import os
# classes = ['Bus', 'Microbus', 'Minivan', 'Sedan', 'SUV', 'Truck']
# images_annotatins = ['images','annotations']
# original_path = 'D:\python_file\dataset\make_dateset\datasetv2.0'
# for car in classes:
#     original_images_path = original_path+"\\"+car+"\\"+images_annotatins[0]
#     original_xml_path = original_path+"\\"+car+"\\"+images_annotatins[1]
#     list  = os.listdir(original_images_path)
#     print(len(list))
#     print(original_xml_path,"\t",original_images_path)
#
# import cv2
#
# original_images_path = r"D:\python_file\dataset\make_dateset\TEST_DATASET\Bus\images\Bus_10.jpg"
# original_image_cv2 = cv2.imread(original_images_path)
# cv2.imshow("original",original_image_cv2)
# print("original image shape",original_image_cv2.shape)
# x, y = 0.6, 0.6
# original_y, original_x = original_image_cv2.shape[:2]
# resize_image = cv2.resize(original_image_cv2,
#                           (int(original_x * x),
#                            int(original_y * y)),
#                           interpolation=cv2.INTER_CUBIC)
# print(resize_image.shape)
# cv2.imshow("resize",resize_image)
#
# x, y = 1, 1
# original_y, original_x = original_image_cv2.shape[:2]
# resize_image2 = cv2.resize(resize_image,
#                           (int(original_x * x),
#                            int(original_y * y)),
#                           interpolation=cv2.INTER_CUBIC)
# print("shape",resize_image2.shape)
# cv2.imshow("resize2",resize_image2)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print