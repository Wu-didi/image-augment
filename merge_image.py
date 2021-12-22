# Standard imports
import cv2
import numpy as np 

ImgPath = r'D:\python_files4\compition\yolov5-master\yolov5-master\data\data\train_images\299.png'
ImgPath2 = r'D:\python_files4\compition\yolov5-master\yolov5-master\data\data\train_images\283.png'

# Read images
src = cv2.imread(ImgPath2)
dst = cv2.imread(ImgPath)

# Create a rough mask around the airplane.
src_mask = np.zeros(src.shape, src.dtype)

# 当然我们比较懒得话，就不需要下面两行，只是效果差一点。
# 不使用的话我们得将上面一行改为 mask = 255 * np.ones(obj.shape, obj.dtype) <-- 全白
poly = np.array([ [4,80], [30,54], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))

# 这是 飞机 CENTER 所在的地方
center = (80,10)

# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)

# 保存结果
cv2.imwrite("opencv-seamless-cloning-example.jpg", output)
