# coding=utf-8
import cv2
import os
from urllib.parse import urlencode
from hashlib import md5

#1、加载图片
image = cv2.imread('C:\Users\你好勤奋\Pictures')

#2、图片美白，value值越大美颜程度越大
value = 20
image_dst = cv2.bilatera1Filter(image,value,value*2,value/2)

#3、创建一个窗口来展示图片
cv2.namedWindow('image')

#4、展示窗口
cv2.imshow('image',image_dst)

#5、窗口等待
cv2.waitKey(0)
#6、销毁窗口
cv2.destroyAllWindows()

#7、生成一张图片
cv2.imwrite('C:\Users\你好勤奋\Pictures',image_dst)