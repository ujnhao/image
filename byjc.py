#!/usr/bin/env python2.7
#coding=utf-8
#https://www.cnblogs.com/lynsyklate/p/7881300.html
#图像边缘检测Sobel算子

from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import sys
import numpy as np



def SobelOperator(roi,operator_type):
    if operator_type == "horizontal":
        sobel_operator = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    elif operator_type == "vertical":
        sobel_operator = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    else:
        raise("type Error")
    result = np.abs(np.sum(roi*sobel_operator))
    return result
    
def SobelAlogrithm(image, operator_type):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_DEFAULT)
    for i in range(1, image.shape[0]-1):
        for j in range(1, image.shape[1]-1):
            new_image[i-1,j-1] = SobelOperator(image[i-1:i+2,j-1:j+2],operator_type)
    new_image = new_image*(255/np.max(image))
    return new_image.astype(np.uint8)

plt.subplot(121)
plt.title("horizontal")
plt.imshow(SobelAlogrithm(gray_saber,"horizontal"),cmap="binary")
plt.axis("off")
plt.subplot(122)
plt.title("vertical")
plt.imshow(SobelAlogrithm(gray_saber,"vertical"),cmap="binary")
plt.axis("off")
plt.show()

