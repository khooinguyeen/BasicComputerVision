#5

import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/starry_sky.jpg')

cv.imshow('Starry sky', img) 

# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 170, -273)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2] # 2 giá trị đầu của img.shape (chiều cao, chiều dài)

    if rotPoint is None:                    # rotPoint là tâm xoay. Nếu rỗng thì mặc định đấy là tâm ảnh
        rotPoint = (width//2, height//2) 

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(translated, 45)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)  

# thu nhỏ --> cv.INTER_AREA
# phóng to --> cv.INTER_CUBIC or cv.INTER_LINEAR (cubic chất lg cao hơn nma lâu hơn)

cv.imshow('Resized', resized)

# Flipping
flipped = cv.flip(img, -1) # 0, -1, 1 để flip theo chiều ngang, dọc ctct
cv.imshow('Flipped', flipped)

# Cropping
cropped = img[100:200, 200:300]
cv.imshow('Cropped', cropped)

cv.waitKey(0)