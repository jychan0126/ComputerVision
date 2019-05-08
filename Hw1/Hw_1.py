# -*- coding: UTF-8 -*-
'''
Created on 2018/9/12

@author: Chan Ju-Ying
'''
import numpy
# import cv2 as cv

from PIL import Image
# from matplotlib import pyplot as plt


img = Image.open('Lena.jpg')

height, width = img.size
Array = numpy.array(img)
# print(Array.shape)

# ---------------------

UpsideDown_Array = Array[::-1]
UpsideDownimg = Image.fromarray(UpsideDown_Array)
UpsideDownimg.save('Lena_UpsideDown.jpg')

# ---------------------

RightSideLeft_Array = Array[::, ::-1]
RightSideLeftimg = Image.fromarray(RightSideLeft_Array)
RightSideLeftimg.save('RightSideLeft.jpg')

# ----------------------

DDiagonallyMirroredArray = numpy.zeros(Array.shape, dtype = Array.dtype)
UDiagonallyMirroredArray = numpy.zeros(Array.shape, dtype = Array.dtype)

for i in range(height):
    for j in range(i + 1):
 
        UDiagonallyMirroredArray[j][i] = Array[j][i]
        UDiagonallyMirroredArray[i][j] = Array[j][i]
        
        DDiagonallyMirroredArray[i][j] = Array[i][j]         
        DDiagonallyMirroredArray[j][i] = Array[i][j]

        
DDiagonallyMirroredimg = Image.fromarray(DDiagonallyMirroredArray)
UDiagonallyMirroredimg = Image.fromarray(UDiagonallyMirroredArray)
DDiagonallyMirroredimg.save('DDiagonallyMirrored.jpg')
UDiagonallyMirroredimg.save('UDiagonallyMirrored.jpg')

# ----------------------

Rotationimg = img.rotate(-45)
Rotationimg.save('Rotation.jpg')

# ----------------------

Halfimg = img.resize((256, 256))
Halfimg.save('Half.jpg')

# ----------------------

Binary_Array = Array

for i in range(height):
    for j in range(width):
        if(Binary_Array[i][j][0] >= 128):
            Binary_Array[i][j] = 255
        else:
            Binary_Array[i][j] = 0
            
Binaryimg = Image.fromarray(Binary_Array)
Binaryimg.save('Binary.jpg')

# ----------------------

print("Complete")

