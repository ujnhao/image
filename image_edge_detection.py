#!/usr/bin/env python2.7
#coding=utf-8
#https://www.cnblogs.com/lynsyklate/p/7881300.html
#图像边缘检测Sobel算子

from math import sqrt
from PIL import Image
import numpy
import sys

filtermatrice_vertical = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
filtermatrice_horizontal = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]

path = sys.argv[1]

im = Image.open(path)
w, h = im.size

pix = numpy.zeros(shape=(w, h, 3), dtype=numpy.uint8)

neighbormatrice = numpy.zeros(shape=(5, 5), dtype=numpy.uint8)  # Neighbor matrix to be filtered pixel

matris_sobel = numpy.zeros(shape=(w, h, 3), dtype=numpy.uint8)

for i in range(w):
    for j in range(h):
        rgb_im = im.convert('RGB')
        r, g, b = rgb_im.getpixel((i, j))
        pix[i][j] = r, g, b
        if(i>=2&i<(w-1)&j>=2&j<(h-1)):
            for m in range(3):
                value_vertical = 0.0
                value_horizontal = 0.0
                for k in range(3):
                    for l in range(3):
                        neighbormatrice[k][l] = pix[k + i-2][l + j - 2][m]  # Create neighbor matrice's indexs(except a frame size=2)
                        value_vertical += neighbormatrice[k][l] * filtermatrice_vertical[k][l]
                        value_horizontal += (neighbormatrice[k][l] * filtermatrice_horizontal[k][l])
                value = sqrt((value_vertical**2) + (value_horizontal**2))
                matris_sobel[i][j][m] = int(value)

img = Image.fromarray(matris_sobel, 'RGB')  # Create an image with RGB values
img.save("target.jpg")
img.show()
