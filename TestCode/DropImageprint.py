# _*_ coding: utf-8 _*_
# @Time : 2021/8/5/0005 22:01 
# @Author : 流柯 
# @Version：V 0.1
# @File : DropImageprint.py
# @desc : 去除照片里面的水印


import cv2
import numpy as np
path = "a.jpg"   #记得不要有中文路径

img = cv2.imread(path)
height,width = img.shape[0:2]
print(height, width)

thresh = cv2.inRange(img, np.array([0,0,0]), np.array([192, 192, 192]))
# 开始腐蚀图片
scan = np.ones((3,3), np.uint8)
print(scan)
cor = cv2.dilate(thresh,scan,iterations=1)

specular = cv2.inpaint(img,cor,5,flags=cv2.INPAINT_TELEA)

# cv2.namedWindow("image",0)
# cv2.resize(img,(int(width/2),int(height/2)))
# cv2.imshow("image",img)
# cv2.waitKey()
# cv2.destroyAllWindows()

cv2.namedWindow("modified",0)
cv2.resize(specular,(int(width/2),int(height/2)))
cv2.imshow("modified",specular)
cv2.waitKey()
cv2.destroyAllWindows()