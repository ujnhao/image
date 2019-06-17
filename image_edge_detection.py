#!/usr/bin/env python2.7
#coding=utf-8
#图像边缘检测Sobel算子

from math import sqrt
from PIL import Image
import numpy
import sys


def func_image(path):
    filtermatrice_vertical = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    filtermatrice_horizontal = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]

    image = Image.open(path)
    image.show()
    w, h = image.size

    pix = numpy.zeros(shape=(w, h, 3), dtype = numpy.uint8)
    neighbormatrice = numpy.zeros(shape=(5, 5), dtype = numpy.uint8)  # Neighbor matrix to be filtered pixel
    matris_sobel = numpy.zeros(shape=(w, h, 3), dtype = numpy.uint8)

    for i in range(w):
        for j in range(h):
            rgb_im = image.convert('RGB')
            r, g, b = rgb_im.getpixel((i, j))
            pix[i][j] = r, g, b
            if(i >= 2 & i < (w - 1) & j >= 2 & j < (h - 1)):
                for m in range(3):
                    value_vertical = 0.0
                    value_horizontal = 0.0
                    for k in range(3):
                        for l in range(3):
                            neighbormatrice[k][l] = pix[k + i - 2][l + j - 2][m]
                            value_vertical += neighbormatrice[k][l] * filtermatrice_vertical[k][l]
                            value_horizontal += (neighbormatrice[k][l] * filtermatrice_horizontal[k][l])
                    value = sqrt((value_vertical ** 2) + (value_horizontal ** 2))
                    matris_sobel[i][j][m] = int(value)

    image = Image.fromarray(matris_sobel, 'RGB')
    image.save("target.jpg")
    image.show()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        func_image(sys.argv[1])
