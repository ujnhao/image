#!/usr/bin/env python2.7
#coding=utf-8
#https://blog.csdn.net/fffupeng/article/details/73463749
#图像直方图均衡化算法

from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import sys
import numpy as np

 
img = Image.open('./data/1600.jpg') 
img_gray = img.convert('L')#将图像转为灰度，减少计算的维度
img_gray_array = np.array(img_gray)

img_gray.show('img_gray')
w = img_gray_array.shape[0]
h = img_gray_array.shape[1]

print(img_gray_array)
import matplotlib.pyplot as plt
 
p1 = plt.hist(img_gray_array.reshape(img_gray_array.size, 1))
 
#plt.subplot(121) 
plt.show()
 
#创建直方图
n = np.zeros((256),dtype = np.float)
p = np.zeros((256),dtype = np.float)
c = np.zeros((256),dtype = np.float)

#遍历图像的每个像素,得到统计分布直方图 
for x in range(0,img_gray_array.shape[0]):
    for y in range(0,img_gray_array.shape[1]):
        #print im_gray[x][y]
        n[img_gray_array[x][y]] += 1
print n
 
#归一化
 
for i in range(0,256):
    p[i] = n[i]/float(img_gray_array.size)
 
#计算累积直方图
c[0] = p[0]
for i in range(1,256):
    c[i] = c[i-1]+p[i]
print c
 
des = np.zeros((w,h),dtype=np.uint8)
 
for x in range(0,w):
    for y in range(0,h):
        des[x][y] = 255*c[img_gray_array[x][y]]
print des

#Image.show('des',des)
p2 = plt.hist(des.reshape(des.size,1))
#plt.subplot(121)
plt.show()
