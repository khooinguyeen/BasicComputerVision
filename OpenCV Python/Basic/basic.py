#4

import cv2 as cv

img = cv.imread('OpenCV Python/Photos/snow.jpg')
cv.imshow('Snow', img)

# Converting to gray scale (đen trắng)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
cv.imshow('Gray', gray)

# Blur (làm mờ)
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade (Viền cạnh, liên quan đến threshold)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating (làm dày viền)
dilated = cv.dilate(canny, (7, 7), iterations = 3)
cv.imshow('Dilated', dilated)

# Eroding (làm mỏng viền)
eroded = cv.erode(dilated, (3, 3), iterations = 2)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 250), interpolation = cv.INTER_AREA) # nếu resize ảnh to thì dùng INTER_LINEAR hoặc INTER_CUBIC sẽ rõ hơn 
cv.imshow('Resized', resized)                                       # dài trước rộng sau

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)