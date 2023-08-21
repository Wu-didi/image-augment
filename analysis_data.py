import os
import pandas as pd
import  shutil

# data_root_path = 'phase2_train/phase2_train_sorted.csv'
# image_root_path = 'phase2_train/phase2_train'
# save_root_path = 'phase2_train/phase2_train_color'
# # 原始数据
# data = pd.read_csv(data_root_path)
# print(data)
# image_ids= data['id']
# image_types= data['color']
# type_num = data["color"].value_counts()#所有的车型
# for one_image_name,one_image_type in zip(image_ids,image_types):
#
#     one_image_path = os.path.join(image_root_path,one_image_name)
#     save_image_path = os.path.join(save_root_path,one_image_type,one_image_name)
#     print(one_image_path)
#     print(save_image_path)
#     if not os.path.exists(os.path.join(save_root_path,one_image_type)):
#         os.makedirs(os.path.join(save_root_path,one_image_type))
#     shutil.copy(one_image_path,save_image_path)
import random
save_root_path = 'F:\APP\BaiduNetdiskDownload\detect_car\detect_car\dataset\phase2_train\phase2_aug_data_color/white'
name = os.listdir(save_root_path)
print(len(name))
random.shuffle(name)
# for i in name[:2000]:
#
#     os.remove(os.path.join(save_root_path, i))
#
# print(name)
#
